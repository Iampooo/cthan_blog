---
type: "note"          
title: "Markdown Test"    
date: 2026-03-11
lang: "en" 
tags: ["note"]
draft: true
---
# h1 Heading 
## h2 Heading
### h3 Heading
#### h4 Heading
##### h5 Heading
###### h6 Heading


## Horizontal Rules

___

---

***

## Emphasis

**This is bold text**

__This is bold text__

***This is italic text***

_This is italic text_

~~Strikethrough~~

## Callouts
<div class="callout callout-note">
<div class="callout-title">Note</div>
</div>


<div class="callout callout-tldr">
<div class="callout-title">Tldr</div>
</div>


<div class="callout callout-info">
<div class="callout-title">Info</div>
</div>


<div class="callout callout-todo">
<div class="callout-title">Todo</div>
</div>


<div class="callout callout-tip">
<div class="callout-title">Tip</div>
</div>


<div class="callout callout-success">
<div class="callout-title">Success</div>
</div>


<div class="callout callout-question">
<div class="callout-title">Question</div>
</div>


<div class="callout callout-warning">
<div class="callout-title">Warning</div>
</div>


<div class="callout callout-fail">
<div class="callout-title">Fail</div>
</div>


<div class="callout callout-danger">
<div class="callout-title">Danger</div>
</div>


<div class="callout callout-bug">
<div class="callout-title">Bug</div>
</div>


<div class="callout callout-example">
<div class="callout-title">Example</div>
</div>


<div class="callout callout-quote">
<div class="callout-title">Quote</div>
</div>


<div class="callout callout-info">
<div class="callout-title">Info</div>
<div class="callout-content">

人物介紹

</div>
</div>

## Blockquotes


> Blockquotes can also be nested...
>> ...by using additional greater-than signs right next to each other...
> > > ...or with spaces between arrows.


## Lists

Unordered

+ Create a list by starting a line with `+`, `-`, or `*`
+ Sub-lists are made by indenting 2 spaces:
  - Marker character change forces new list start:
    * Ac tristique libero volutpat at
    + Facilisis in pretium nisl aliquet
    - Nulla volutpat aliquam velit
+ Very easy!

Ordered

1. Lorem ipsum dolor sit amet
2. Consectetur adipiscing elit
3. Integer molestie lorem at massa 
4. You can use sequential numbers...
1. ...or keep all the numbers as `1.`

Start numbering with offset:

57. foo
1. bar


## Code

Inline `code`

Indented code

    // Some comments
    line 1 of code
    line 2 of code
    line 3 of code


Block code "fences"

```
Sample text here...
```

Syntax highlighting

``` js
var foo = function (bar) {
  return bar++;
};

console.log(foo(5));
```

``` sol
// SPDX-License-Identifier: GPL-3.0

pragma solidity >= 0.8.4;

contract Array {
    uint256[] arr_1;
    uint256[] arr_2 = [3,2,4];
    uint256[5] arr_3;
    uint256[][] array2D = [ [1,2,3], [4,5,6] ];

    constructor(uint256 _dynamicArrayLength) {
        arr_1 = new uint256[](_dynamicArrayLength);
    }

    function getValueOfIndex(uint256 _index) public view returns (uint256) {
        return arr_2[_index];
    }

    function addToArray(uint256 _value) public {
        arr_2.push(_value);
    }

    function valueCount() public view returns(uint256) {
        return arr_3.length;
    }

    function dynamicValueCount() public view returns(uint256) {
        return arr_1.length;
    }
}

```
## Tables

| Option | Description |
| ------ | ----------- |
| data   | path to data files to supply the data that will be passed into templates. |
| engine | engine to be used for processing templates. Handlebars is the default. |
| ext    | extension to be used for dest files. |

Right aligned columns

| Option | Description |
| ------:| -----------:|
| data   | path to data files to supply the data that will be passed into templates. |
| engine | engine to be used for processing templates. Handlebars is the default. |
| ext    | extension to be used for dest files. |


## Links

[link text](http://dev.nodeca.com)

[link with title](http://nodeca.github.io/pica/demo/ "title text!")

Autoconverted link https://github.com/nodeca/pica (enable linkify to see)


## Images

![Minion](https://octodex.github.com/images/minion.png)
![Stormtroopocat](https://octodex.github.com/images/stormtroopocat.jpg "The Stormtroopocat")

Like links, Images also have a footnote style syntax

![Alt text][id]

With a reference later in the document defining the URL location:

[id]: https://octodex.github.com/images/dojocat.jpg  "The Dojocat"


## Plugins

The killer feature of `markdown-it` is very effective support of
[syntax plugins](https://www.npmjs.org/browse/keyword/markdown-it-plugin).


### [Emojies](https://github.com/markdown-it/markdown-it-emoji)

> Classic markup: :wink: :crush: :cry: :tear: :laughing: :yum:
>
> Shortcuts (emoticons): :-) :-( 8-) ;)

see [how to change output](https://github.com/markdown-it/markdown-it-emoji#change-output) with twemoji.


### [Subscript](https://github.com/markdown-it/markdown-it-sub) / [Superscript](https://github.com/markdown-it/markdown-it-sup)

- 19^th^
- H~2~O


### [\<ins>](https://github.com/markdown-it/markdown-it-ins)

++Inserted text++


### [\<mark>](https://github.com/markdown-it/markdown-it-mark)

==Marked text==


### [Footnotes](https://github.com/markdown-it/markdown-it-footnote)

Footnote 1 link[^first].

Footnote 2 link[^second].

Inline footnote^[Text of inline footnote] definition.

Duplicated footnote reference[^second].

[^first]: Footnote **can have markup**

    and multiple paragraphs.

[^second]: Footnote text.


### [Definition lists](https://github.com/markdown-it/markdown-it-deflist)

Term 1

:   Definition 1
with lazy continuation.

Term 2 with *inline markup*

:   Definition 2

        { some code, part of Definition 2 }

    Third paragraph of definition 2.

_Compact style:_

Term 1
  ~ Definition 1

Term 2
  ~ Definition 2a
  ~ Definition 2b


### [Abbreviations](https://github.com/markdown-it/markdown-it-abbr)

This is HTML abbreviation example.

It converts "HTML", but keep intact partial entries like "xxxHTMLyyy" and so on.

*[HTML]: Hyper Text Markup Language

### [Custom containers](https://github.com/markdown-it/markdown-it-container)

::: warning
*here be dragons*
:::

[^1]: hwoe
