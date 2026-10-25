---
task_id: "783f4796-ebeb-4084-a4e7-58da3edd4238"
title: "leetcode questions"
status: "todo"
priority: "high"
duration: 60
due: "2026-10-22"
scheduled: "2026-10-22"
is_all_day: true
tags:
  - "python"
  - "math"
group: "Inbox"
created: "2026-10-21T19:25:26.679Z"
modified: "2026-10-21T19:25:58.277Z"
kanban-id: "2a47dd24-cfe5-466f-8484-f1800168f892"
rrule: "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR,SA"
repeat_id: "c6061048-7fda-417b-97ac-d0453d8f1d8e"
type: "task"
milestone: true
kanban_name: "ezz"
kanban_columns:
  - "To Do"
  - "In Progress"
  - "Done"
---

### Activity Heatmap
```tasks-heatmap
```

### Repeat Occurrences
```base
properties:
  file.name:
    displayName: Task
  note.due:
    displayName: Due Date
  note.status:
    displayName: Status
views:
  - type: table
    name: History
    filters:
      and:
        - repeat_parent_id.contains(this.file.properties.repeat_id)
    sort:
      - property: due
        direction: DESC
```