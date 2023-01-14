---
theme: seriph
background: https://source.unsplash.com/collection/94734566/1920x1080
class: 'text-center'
highlighter: shiki
lineNumbers: false
info: |
  ## sm_city
  Presentation sm_city solution.

drawings:
  persist: false
css: unocss
---

# sm_city

Presentation

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    Press Space for next page <carbon:arrow-right class="inline"/>
  </span>
</div>

<div class="abs-br m-6 flex gap-2">
  <button @click="$slidev.nav.openInEditor()" title="Open in Editor" class="text-xl icon-btn opacity-50 !border-none !hover:text-white">
    <carbon:edit />
  </button>
  <a href="https://github.com/slidevjs/slidev" target="_blank" alt="GitHub"
    class="text-xl icon-btn opacity-50 !border-none !hover:text-white">
    <carbon-logo-github />
  </a>
</div>

<!--
The last comment block of each slide will be treated as slide notes. It will be visible and editable in Presenter Mode along with the slide. [Read more in the docs](https://sli.dev/guide/syntax.html#notes)
-->

---

# Diagrams

Solution overview

<div class="grid grid-cols-3 gap-10 pt-4 -mb-6">

```mermaid {theme: 'neutral', scale: 0.8}
graph TD
B[IP Camera] --> C[Image Spool]
C --> D[Backend]
D --> E[Database]
D --> F[Queue]
D <--> G[Consumer]
D <--> H[Front-end]
G <--> F
```

</div>
