# General Misc Snippets

## Date and Time Regex (mostly logs)

```
(?P<year>\d\d\d\d).?(?P<month>[01]\d).?(?P<day>[0123]\d).*?(?P<hour>[012]\d).?(?P<minute>[0123456]\d).?(?P<second>[0123456]\d)
```
