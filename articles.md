---
title: Articles and essays
layout: page
---

An outlet for thoughts...

<table style="width: 100%">
  {% for post in site.posts %}
    <tr>
      <td style="text-align: right;">{{ post.date | date: "%b %d" }}</td>
      <td style="text-align: left;"><a href="{{ post.url }}">{{ post.title }}</a></td>
      <td style="text-align: right;"><em>{{ post.date | date: "%Y" }}</em></td>
    </tr>
  {% endfor %}
</table>
