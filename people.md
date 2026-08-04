---
title: People
permalink: /people/
description: "Meet the members of the OptimalX research group at the University of Minnesota Twin Cities — PhD students, undergraduate researchers, and alumni working on optimal control and autonomous systems."
---
<br>
{% assign people_sorted = site.people | sort: 'joined' %}
{% assign role_array = "pi|postdoc|phdstudent|gradstudent|undergrad|researchstaff|visiting|others" | split: "|" %}

{% for role in role_array %}

{% assign people_in_role = people_sorted | where: 'position', role %}

<!-- Skip section if there's nobody -->
{% if people_in_role.size == 0 %}
  {% continue %}
{% endif %}

<div class="pos_header">
{% if role == 'postdoc' %}
<h3>Postdoctoral Fellows</h3>
 {% elsif role == 'pi' %}
<h3>Principal Investigator</h3>
 {% elsif role == 'phdstudent' %}
<h3>Ph.D. Students</h3>
 {% elsif role == 'gradstudent' %}
<h3>Graduate Students</h3>
 {% elsif role == 'undergrad' %}
<h3>Undergraduate Students</h3>
 {% elsif role == 'researchstaff' %}
<h3>Research Staff</h3>
 {% elsif role == 'visiting' %}
<h3>Visiting Scholars</h3>
 {% elsif role == 'others' %}
<h3>Honorary Members</h3>
{% endif %}
</div>

<div class="content list people">
  {% for profile in people_sorted %}
    {% if profile.position contains role %}
      <div class="list-item-people">
        <p class="list-post-title">
          {% if profile.avatar %}
            <a href="{{ site.baseurl }}{{ profile.url }}"><img class="profile-thumbnail" src="{{site.baseurl}}/images/people/{{profile.avatar}}"></a>
          {% else %}
            <a href="{{ site.baseurl }}{{ profile.url }}"><img class="profile-thumbnail" src="http://evansheline.com/wp-content/uploads/2011/02/facebook-Storm-Trooper.jpg"></a>
          {% endif %}
          <a class="name" href="{{ site.baseurl }}{{ profile.url }}">{{ profile.name }}</a>
        </p>
      </div>
    {% endif %}
  {% endfor %}
</div>
<hr>

{% endfor %}

<div class="pos_header">
<h3>Alumni</h3>
</div>

<br>

| Name | Current Position |
| :--- | :--- |
| [Amanuel Adane](https://www.linkedin.com/in/amanuel-adane-b214501b8/) | Student at Cornell University |
| [Shaumik Kalwit](https://www.linkedin.com/in/shaumikkalwit/) | CS Student at UMN, IBM Intern |
| Pengyang Li | Student at UC Berkeley |
