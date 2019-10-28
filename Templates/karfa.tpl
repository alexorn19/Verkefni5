{% extends "base.html" %}

{% block innihald %}

		<h1>Karfa:</h1>

		{% for i in valdarvorur %}
			<h5> {{ vorur[i][1] }} {{ vorur[i][2] }} </h5>
		{% endfor%}

{% endblock %}
