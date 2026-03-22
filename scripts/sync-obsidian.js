import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const PROJECT_ROOT = path.resolve(__dirname, '..');

// ── Config ──────────────────────────────────────────────────────────
const OBSIDIAN_VAULT_ROOT = 'C:/Users/user/Iampoo/obsidian_vault';
const OBSIDIAN_ATTACHMENTS = path.join(OBSIDIAN_VAULT_ROOT, '00 Obsidian', '002 Attachments');
const ASTRO_ARTICLES = path.join(PROJECT_ROOT, 'src', 'content', 'articles');
const ASTRO_IMAGES = path.join(PROJECT_ROOT, 'public', 'images', 'articles');

// ── Main ────────────────────────────────────────────────────────────
let srcFile = process.argv[2];
if (!srcFile) {
  console.error('Usage: npm run sync -- <filename-or-path> [slug]');
  console.error('Example: npm run sync -- "My Note"');
  console.error('Example: npm run sync -- "C:/Users/user/Iampoo/obsidian_vault/My Note.md" my-slug');
  console.error('\n* "slug" is the URL-friendly name for the post (e.g., "lessons-with-sani-1").');
  process.exit(1);
}

// Handle relative/filename-only input
let absSource = path.resolve(srcFile);
if (!fs.existsSync(absSource)) {
  // If not absolute or not found, try in Obsidian Vault
  const vaultPath = path.join(OBSIDIAN_VAULT_ROOT, srcFile.endsWith('.md') ? srcFile : `${srcFile}.md`);
  if (fs.existsSync(vaultPath)) {
    absSource = vaultPath;
  } else {
    // Also try without forcing .md if it already has an extension
    const vaultPathRaw = path.join(OBSIDIAN_VAULT_ROOT, srcFile);
    if (fs.existsSync(vaultPathRaw)) {
      absSource = vaultPathRaw;
    } else {
      console.error(`❌ File not found at ${absSource} or ${vaultPath}`);
      process.exit(1);
    }
  }
}

// Determine output filename (Slug)
// Strict slug: remove Chinese characters, allow only lowercase alphanumeric + dashes
const generateSlug = (name) => {
  return name
    .toLowerCase()
    .trim()
    .replace(/[\u4e00-\u9fa5]+/g, '')          // Remove Chinese characters
    .replace(/[\s\t\n\r]+/g, '-')              // Spaces to dashes
    .replace(/[^a-z0-9-]+/g, '')               // Remove everything else except a-z, 0-9, and -
    .replace(/-+/g, '-')                      // Collapse multiple dashes
    .replace(/^-|-$/g, '');                   // Trim dashes from start/end
};

const baseName = path.basename(absSource, '.md');
const outputSlug = process.argv[3] || generateSlug(baseName);
const outputFile = path.join(ASTRO_ARTICLES, `${outputSlug}.md`);

console.log(`📖 Source:  ${absSource}`);
console.log(`📝 Output:  ${outputFile}`);

let content = fs.readFileSync(absSource, 'utf-8');

// ── 0. Handle Title & Frontmatter ──────────────────────────────────
content = processFrontmatter(content, baseName);

// ── 1. Convert image embeds ────────────────────────────────────────
// ![[image.png]] or ![[image.png|600]]
fs.mkdirSync(ASTRO_IMAGES, { recursive: true });

content = content.replace(/!\[\[([^\]|]+?)(?:\|[^\]]*?)?\]\]/g, (_match, filename) => {
  const imgSrc = path.join(OBSIDIAN_ATTACHMENTS, filename);
  const imgDst = path.join(ASTRO_IMAGES, filename);
  if (fs.existsSync(imgSrc)) {
    fs.copyFileSync(imgSrc, imgDst);
    console.log(`  ✅ Image copied: ${filename}`);
  } else {
    console.warn(`  ⚠️  Image not found: ${imgSrc}`);
  }
  return `![${filename}](/images/articles/${encodeURIComponent(filename)})`;
});

// ── 2. Convert callouts ────────────────────────────────────────────
content = convertCallouts(content);

// ── 3. Strip wikilinks [[Page]] or [[Page|Display]] ────────────────
content = content.replace(/\[\[([^\]|]+?)(?:\|([^\]]*?))?\]\]/g, (_m, target, display) => {
  return display || target;
});

// ── Write output ───────────────────────────────────────────────────
fs.writeFileSync(outputFile, content, 'utf-8');
console.log(`\n🎉 Done! Article written to ${outputFile}`);

// ====================================================================
// Frontmatter & Title Processing
// ====================================================================
function processFrontmatter(text, sourceBaseName) {
  const fmMatch = text.match(/^---\r?\n([\s\S]*?)\r?\n---/);
  
  if (!fmMatch) {
    console.warn('  ⚠️  No frontmatter found! Creating default frontmatter.');
    return `---\ntype: "note"\ntitle: "${sourceBaseName}"\ndate: ${new Date().toISOString().split('T')[0]}\nlang: "zh"\ndraft: false\n---\n\n${text}`;
  }

  let fm = fmMatch[1];
  const body = text.slice(fmMatch[0].length);

  // Update or inject title
  if (/^title:/m.test(fm)) {
    fm = fm.replace(/^title:.*$/m, `title: "${sourceBaseName}"`);
  } else {
    fm = `title: "${sourceBaseName}"\n${fm}`;
  }

  // Ensure other required fields exist (basic validation/injection)
  if (!/^type:/m.test(fm)) fm = `type: "note"\n${fm}`;
  if (!/^date:/m.test(fm)) fm = `date: ${new Date().toISOString().split('T')[0]}\n${fm}`;
  if (!/^lang:/m.test(fm)) fm = `lang: "zh"\n${fm}`;

  return `---\n${fm.trim()}\n---${body}`;
}

// ====================================================================
// Callout Conversion
// ====================================================================
function convertCallouts(text) {
  const lines = text.split('\n');
  const result = [];
  let i = 0;

  while (i < lines.length) {
    // Check if this line starts a callout: > [!type]
    const headerMatch = lines[i].match(/^>\s*\[!(\w+)\][+-]?\s*(.*)?$/i);
    if (!headerMatch) {
      result.push(lines[i]);
      i++;
      continue;
    }

    const calloutType = headerMatch[1].toLowerCase();
    const titleText = (headerMatch[2] || '').trim();
    i++;

    // Collect callout body lines (lines starting with > )
    const bodyLines = [];
    while (i < lines.length && /^>/.test(lines[i])) {
      // Strip the leading > and optional single space
      bodyLines.push(lines[i].replace(/^>\s?/, ''));
      i++;
    }

    const body = bodyLines.join('\n').trim();

    // Special rendering for [!quote]
    if (calloutType === 'quote' && titleText) {
      result.push(`<div class="styled-quote">`);
      result.push(`<div class="styled-quote-mark">"</div>`);
      result.push(`<div class="styled-quote-text">`);
      result.push('');
      result.push(body);
      result.push('');
      result.push(`</div>`);
      result.push(`<div class="styled-quote-source">－ ${titleText}</div>`);
      result.push(`</div>`);
      result.push('');
    } else {
      // General callout
      const displayType = calloutType.charAt(0).toUpperCase() + calloutType.slice(1);
      const fullTitle = titleText ? `${displayType}: ${titleText}` : displayType;

      result.push(`<div class="callout callout-${calloutType}">`);
      result.push(`<div class="callout-title">${fullTitle}</div>`);
      if (body) {
        result.push(`<div class="callout-content">`);
        result.push('');
        result.push(body);
        result.push('');
        result.push(`</div>`);
      }
      result.push(`</div>`);
      result.push('');
    }
  }

  return result.join('\n');
}
