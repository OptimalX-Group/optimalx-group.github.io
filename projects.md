---
title: Projects
permalink: /projects/
description: "Research projects from the OptimalX group at University of Minnesota, spanning trajectory optimization, multi-agent systems, game theory, advanced air mobility, and space robotics."
---

### Nonlinear Trajectory Optimization for UAVs with Multiple Task Positions

TBD

### In-House Robot Platforms

We design and build our own aerial and ground robots to test our planning and control algorithms on real hardware. Below are test trajectories run in our motion-capture lab; each video includes an inset showing the planned path and the robot's tracked motion.

#### Quadrotor

<div class="video-gallery">
  <figure>
    <video autoplay muted loop playsinline controls poster="{{ '/images/videos/quadrotor_square.jpg' | relative_url }}">
      <source src="{{ '/images/videos/quadrotor_square.mp4' | relative_url }}" type="video/mp4">
    </video>
    <figcaption>Square trajectory</figcaption>
  </figure>

  <figure>
    <video autoplay muted loop playsinline controls poster="{{ '/images/videos/quadrotor_circle.jpg' | relative_url }}">
      <source src="{{ '/images/videos/quadrotor_circle.mp4' | relative_url }}" type="video/mp4">
    </video>
    <figcaption>Circle trajectory</figcaption>
  </figure>
</div>

#### Ground Robot (UGV)

<div class="video-gallery">
  <figure>
    <video autoplay muted loop playsinline controls poster="{{ '/images/videos/ugv_m_logo.jpg' | relative_url }}">
      <source src="{{ '/images/videos/ugv_m_logo.mp4' | relative_url }}" type="video/mp4">
    </video>
    <figcaption>UGV tracing the Minnesota "M"</figcaption>
  </figure>
</div>

<style>
.video-gallery {
  display: flex;
  flex-direction: column;
  gap: 24px;
  margin-bottom: 20px;
}

.video-gallery figure {
  margin: 0;
  text-align: center; /* Centers the caption */
}

.video-gallery video {
  width: 100%;
  height: auto;
  display: block;
  border-radius: 6px;
}

.video-gallery figcaption {
  margin-top: 8px;
  font-style: italic;
  font-size: 1.05em;
}
</style>
