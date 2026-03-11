import { defineCollection, z } from 'astro:content';

const articlesCollection = defineCollection({
    type: 'content',
    schema: z.object({
        type: z.enum(['book', 'essay', 'memo', 'learn']),
        title: z.string(),
        date: z.date(),
        lang: z.enum(['en', 'zh']),
        tags: z.array(z.string()).optional(),
        draft: z.boolean().default(false).optional(),
    }),
});

export const collections = {
    'articles': articlesCollection,
};
