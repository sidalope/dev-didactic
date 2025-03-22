## Contributions

Any contributions to these pages is welcome. This document is a work in progress, so make sure to refer back to it before submitting a pull request. Please reach out to me if you want to talk about this at all. It doesn't have to be an emergency.

Commits follow the [Conventional Commits specification](https://www.conventionalcommits.org/en/v1.0.0/). Commit messages should be structured as follows:

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

<br/>

### Types

When committing code, use the relevant type from the specification above, noting the absence of `ci:` and the addition of `wip:`, i.e. one of:

`fix:`, `feat:`, `wip:`, `build:`, `chore:`, `docs:`, `style:`, `refactor:`, `perf:`, `test:`.

the `wip:` type is uniquely relevant here as we are uploading code that may be functional but ugly, not fully tested, etc. This is a learner's space. Just don't commit anything that doesn't compile or will not run; ❤️ Buggy code that does the thing or some thing vs 💩 crashy code.

<br/>

Since most of this repository will be written in english, most of these tags will often not apply.
When contibuting in english (for example, when contributing to `templates/`, `resources/`, or `dotfiles/`) use the following tags:

`add:`, `corr:`, and `org:`.

`add:` for addition, `corr:` for correction, or `org:` for organization when files and folders have to be deleted or reorganized without changing their content.

<br/>

### Atomic Commits
Remember To keep your commits atomic. For example, when adding `file1.md` and renaming `file1.md` to `file2.md` so that the name `file1.md` will be available, first commit the rename, then the addition, e.g. in order:

```
org: rename file1.md to file2.md

Partition topic X into "file 1" and "file2". Rename file1 to make
space for new resource file2.md.
```

```
add: add new file1.md resource to complement file2
```
probably at this point it would be a good idea to reorganize:

```
org: move topic X files into a new X folder
```

<br/>

### Why even?

This is a whole lot of specificity for something so simple as communicating a change. Why do we use Conventional Commits? From the spec:

> Why Use Conventional Commits
>
>     - Automatically generating CHANGELOGs.
>     - Automatically determining a semantic version bump (based on the types of commits landed).
>     - Communicating the nature of changes to teammates, the public, and other stakeholders.
>     - Triggering build and publish processes.
>     - Making it easier for people to contribute to your projects, by allowing them to explore a more structured commit history.

Some of these just don't apply to this project in this phase, however the third and fifth points are for us more than sufficient. Additionally, explicitly stating a type - and optionally a scope - for every commit helps everyone think atomically and understand Git as more than just a tool for checkpointing and pushing one's work to remote.
