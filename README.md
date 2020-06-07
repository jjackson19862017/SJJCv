
# SJJCv

I have generated a flask app, to make my CV come to life in a web browser.

# Education page - Updated

{% for f in furtEduc %}
<h3>{{f.course}}</h3>
<p>{{f.company}}</p>
<p>Achieved in {{f.achieved}}</p>
<p>Awarded with {{f.result}}</p>
<hr> <!-- Horizontal Rule -->
{% endfor %}
{% for e in educ %}
<h3>{{e.school}}</h3>
<p>{{e.level}}</p>
<p>Achieved in {{e.dateFinished}}</p>
{% if e.awarded == "2" %}
<p><i class="fas fa-award text-warning"></i><i class="fas fa-award text-warning"></i> {{e.subject}}</p>
{% else %}
<p><i class="fas fa-award text-warning"></i> {{e.subject}}</p>
{% endif %}
{% if loop.index != loop.length%}
<hr> <!-- Horizontal Rule -->
{% endif %}
{% endfor %}