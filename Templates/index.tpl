{% extends "base.html" %}

{% block innihald %}

		<h1>Vörulistinn:</h1>

		{% for i in v %}
			<h5> {{ i[1] }} <a href="/kaupa/{{ i[0] }}">{{ i[2] }}</a></h5>
		{% endfor%}

{% endblock %}
