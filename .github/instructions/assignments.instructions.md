---
description: "Instructions to use whenever creating or editing assignment markdown files to ensure consistency and clarity for students."
applyTo: "assignments/**/*.md"
---

# Assignment Markdown Structure Guidelines

All assignment markdown files should follow these guidelines:

## 1. Template Usage

- Assignment markdown files must follow the structure in [`templates/assignment-template.md`](../../templates/assignment-template.md).
- The assignment must be created as a `README.md` file
- Do not remove, rename, reorder, or skip required sections from the template.
- Keep the template's heading levels and icons exactly as written:
  - `# 📘 Assignment: [Assignment Title]`
  - `## 🎯 Objective`
  - `## 📝 Tasks`
  - `### 🛠️ [Task Title]`
  - `#### Description`
  - `#### Requirements`

The completed assignment should use this structure:

```markdown
# 📘 Assignment: [Assignment Title]

## 🎯 Objective

[Brief description of what the student will build or accomplish]

## 📝 Tasks

### 🛠️ [Task Title]

#### Description
[Description of what the student needs to do]

#### Requirements
Completed program should:

- [Requirement 1]
- [Requirement 2]
```

## 2. Section Guidance

The section headers must reflect the structure in the template, including the exact icon usage.

- **Title**: Replace `[Assignment Title]` with a short, descriptive name (e.g., `Python Basics`, `Loops and Conditionals`, `Functions and Modules`).
- **Objective**: Write 1-2 sentences summarizing what the student will learn or accomplish. Focus on the main skills or concepts.
- **Tasks**: Include one or more focused tasks. For each task:
   - Use a specific, action-oriented task name
   - In `Description`, clearly state what the student must do.
   - In `Requirements`, use bullet points to list specific, measurable expected outcomes or features.
   - Provide example input/output in fenced code blocks when helpful.

Do not include extra top-level sections or replace the template structure unless explicitly specified.