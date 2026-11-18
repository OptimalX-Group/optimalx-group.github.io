---
title: Projects
permalink: /projects/
description: "Research projects from the OptimalX group at University of Minnesota, spanning trajectory optimization, multi-agent systems, game theory, advanced air mobility, and space robotics."
---

<div class="projects-hero">
  <h1>Projects</h1>
  <p>Optimization for intelligent decision-making in complex, large-scale autonomous systems.</p>
</div>

<section class="project-section" id="filter-warm-starting">
  <div class="project-head">
    <span class="project-number">01</span>
    <div>
      <h2>Filter-Based Warm-Starting for Multiagent Trajectory Optimization</h2>
      <p class="project-subtitle">Particle filtering finds a good initial guess, and SCP turns it into a safe, optimal trajectory.</p>
    </div>
  </div>

  <div class="project-overview">
    <p>Planning trajectories for multiple agents, such as quadrotors sharing the same airspace, requires solving nonconvex optimization problems with collision avoidance constraints. Iterative solvers such as sequential convex programming (SCP) are sensitive to their initial guess, and a poor guess leads to slow convergence or a suboptimal solution. In addition, many existing methods enforce constraints only at discretization points, so the resulting trajectories can violate them in between.</p>
    <p>Our key idea is to exploit the equivalence between optimal control and optimal estimation. We approximate the trajectory optimization problem as a Bayesian state estimation problem and solve it with constraint-aware particle filtering. The resulting estimate is an efficient approximation of the optimal trajectory, and it serves as a warm start for the optimizer.</p>
  </div>

  <div class="project-results">
    <div class="project-showcase">
      <div class="project-showcase-copy">
        <p class="project-kicker">Warm start from estimation</p>
        <p>Constraint-aware particle filtering generates candidate trajectories for every agent around the obstacles. We use the resulting estimate to warm-start SCP.</p>
      </div>
      <figure class="project-visual">
        <img src="{{ '/images/projects/filtering_warm_start.gif' | relative_url }}" alt="Candidate trajectories for two agents navigating around obstacles">
        <figcaption>Candidate trajectories for two agents moving from their initial positions (circles) to their final positions (triangles) around obstacles</figcaption>
      </figure>
    </div>

    <div class="project-showcase">
      <div class="project-showcase-copy">
        <p class="project-kicker">Continuous-time constraint satisfaction</p>
        <p>We model the continuous-time constraint violation as auxiliary dynamics, thus ensuring the constraints hold along the entire trajectory, not only at discretization points.</p>
        <ul class="project-facts">
          <li><strong>Results</strong><span>Better solutions found faster than random initialization and off-the-shelf solvers.</span></li>
          <li><strong>Application</strong><span>Multiagent quadrotor trajectory optimization with collision avoidance.</span></li>
        </ul>
        <p class="project-actions">
          <a class="project-action" href="https://arc.aiaa.org/doi/full/10.2514/1.G009548">JGCD 2026 paper</a>
          <a class="project-action" href="https://ieeexplore.ieee.org/abstract/document/11107577">ACC 2025 paper</a>
          <a class="project-action secondary" href="https://arxiv.org/abs/2508.14299">arXiv preprint</a>
        </p>
        <p class="project-note">The arXiv preprint of the JGCD paper includes more detailed derivations.</p>
      </div>
      <figure class="project-visual">
        <img src="{{ '/images/projects/six_agent_quadrotor_3d.png' | relative_url }}" alt="3D trajectories of six quadrotors avoiding two cylindrical obstacles">
        <figcaption>Trajectories of six quadrotors from their initial positions (filled circles) to their final positions (triangles) around two cylindrical obstacles, computed by warm-started SCP with collision avoidance satisfied in continuous time</figcaption>
      </figure>
    </div>
  </div>
</section>

<section class="project-section" id="uav-multiple-task-positions">
  <div class="project-head">
    <span class="project-number">02</span>
    <div>
      <h2>Nonlinear Trajectory Optimization for UAVs with Multiple Task Positions</h2>
      <p class="project-subtitle">Details coming soon.</p>
    </div>
  </div>
</section>

<section class="project-section" id="robot-platforms">
  <div class="project-head">
    <span class="project-number">03</span>
    <div>
      <h2>In-House Robot Platforms</h2>
      <p class="project-subtitle">Aerial and ground robots for testing our algorithms on real hardware.</p>
    </div>
  </div>

  <div class="project-overview">
    <p>We design and build our own aerial and ground robots to test our planning and control algorithms on real hardware. Below are test trajectories run in our motion-capture lab; each video includes an inset showing the planned path and the robot's tracked motion.</p>
  </div>

  <div class="project-results">
    <p class="project-kicker">Quadrotor</p>
    <div class="video-gallery">
      <figure class="project-visual">
        <video autoplay muted loop playsinline controls poster="{{ '/images/videos/quadrotor_square.jpg' | relative_url }}">
          <source src="{{ '/images/videos/quadrotor_square.mp4' | relative_url }}" type="video/mp4">
        </video>
        <figcaption>Square trajectory</figcaption>
      </figure>
      <figure class="project-visual">
        <video autoplay muted loop playsinline controls poster="{{ '/images/videos/quadrotor_circle.jpg' | relative_url }}">
          <source src="{{ '/images/videos/quadrotor_circle.mp4' | relative_url }}" type="video/mp4">
        </video>
        <figcaption>Circle trajectory</figcaption>
      </figure>
    </div>

    <p class="project-kicker">Ground Robot (UGV)</p>
    <div class="video-gallery">
      <figure class="project-visual">
        <video autoplay muted loop playsinline controls poster="{{ '/images/videos/ugv_m_logo.jpg' | relative_url }}">
          <source src="{{ '/images/videos/ugv_m_logo.mp4' | relative_url }}" type="video/mp4">
        </video>
        <figcaption>UGV tracing the Minnesota "M"</figcaption>
      </figure>
    </div>
  </div>
</section>
