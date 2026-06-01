# GIT-workshop-Jun-1-26

Introductory course to git workflows.

## Contribution Workflow (Class Exercise)

In this workshop, each student acts as a contributor to a shared project story.

### 1) Start from the issue

1. Open your assigned issue.
2. Read the story details and acceptance criteria.
3. Confirm which section of the collaborative story you are responsible for.

### 2) Get the repository locally

You can either fork first (recommended for external contributors) or work directly if you already have write access.

#### Option A: Fork + Clone (recommended)

```bash
# On GitHub: click Fork, then clone your fork
git clone https://github.com/<your-user>/GIT-workshop-Jun-1-26.git
cd GIT-workshop-Jun-1-26
git remote add upstream https://github.com/CMC-QCL/GIT-workshop-Jun-1-26.git
```

Replace `<your-user>` with your actual GitHub username.

#### Option B: Clone directly (if you have access)

```bash
git clone https://github.com/CMC-QCL/GIT-workshop-Jun-1-26.git
cd GIT-workshop-Jun-1-26
```

### 3) Create a feature branch

Use a branch name linked to the issue:

```bash
git checkout -b issue-<number>-story-update
```

### 4) Contribute to the collaborative story

1. Edit the story content described by your issue.
2. Keep your change focused and small.
3. Commit with a meaningful message.

```bash
git add .
git commit -m "Update story section for issue #<number>"
```

### 5) Push and open a Pull Request

```bash
git push -u origin issue-<number>-story-update
```

Then on GitHub:
1. Open a Pull Request (PR) to the main repository.
2. Reference the issue in the PR description (for example: `Closes #<number>`).
3. Request review from instructor/classmates.

### 6) Review, merge, and class walkthrough

1. Address PR review comments.
2. Once approved, merge the PR.
3. During class, review the complete story and discuss how each contribution was integrated.

---

## Intentional Merge Conflict Exercise

Goal: learn how conflicts happen and how to resolve them.

### Setup

Two contributors edit the same exact line in the story on different branches.

#### Contributor A

```bash
git checkout -b issue-101-story-line
# Edit the same line in the story
git add .
git commit -m "Contributor A edits story line"
git push -u origin issue-101-story-line
```

Create and merge PR A first.

#### Contributor B

```bash
git checkout -b issue-102-story-line
# Edit the same line in the story differently
git add .
git commit -m "Contributor B edits same story line differently"
git push -u origin issue-102-story-line
```

When Contributor B opens/updates PR B after PR A is merged, GitHub should report a merge conflict.

### Resolve the conflict (Contributor B)

```bash
git fetch origin
git checkout issue-102-story-line
git merge origin/main
```

1. Open conflicted files.
2. Keep the correct final text (or combine both edits if appropriate).
3. Remove conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`).

```bash
git add .
git commit -m "Resolve merge conflict with main"
git push
```

Update PR B and complete review/merge.
