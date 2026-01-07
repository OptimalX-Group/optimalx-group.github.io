---
title: Lab
permalink: /lab/
---

<p><strong>Some glimpses of our lab:</strong></p>

<div class="lab-gallery">
  <figure>
    <img src="{{ '/images/desk_space.jpg' | relative_url }}" alt="Lab photo 1">
    <figcaption>Our main desk area where we brainstorm and collaborate.</figcaption>
  </figure>

  <figure>
    <img src="{{ '/images/mocap_space.jpg' | relative_url }}" alt="Lab photo 2">
    <figcaption>Motion capture space used for tracking experiments and simulations.</figcaption>
  </figure>

  <figure>
    <img src="{{ '/images/robots.jpg' | relative_url }}" alt="Lab photo 3">
    <figcaption>Our Robots!</figcaption>
  </figure>

  <figure>
    <img src="{{ '/images/workbenches.jpg' | relative_url }}" alt="Lab photo 4">
    <figcaption>Workbenches equipped for hands-on experiments and prototyping.</figcaption>
  </figure>
</div>

<style>
.lab-gallery {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  justify-content: center;
}

.lab-gallery figure {
  margin: 0;
  text-align: center; /* Centers the caption */
}

.lab-gallery img {
  max-width: 100%;
  height: auto;
  display: block;
  margin: 0 auto; /* Centers the image */
}

.lab-gallery figcaption {
  margin-top: 8px;
  font-style: italic;
  font-size: 1.05em; /* Slightly bigger than before */
}
</style>
