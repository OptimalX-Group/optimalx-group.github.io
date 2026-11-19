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

<section class="project-section" id="estimation-aware-tracking">
  <div class="project-head">
    <span class="project-number">02</span>
    <div>
      <h2>Continuous-Time Estimation-Aware Optimal Control for Target Tracking</h2>
      <p class="project-subtitle">Mobile sensors plan their motion to reduce estimation uncertainty while satisfying their constraints in continuous time.</p>
    </div>
  </div>

  <div class="project-overview">
    <p>In target tracking, mobile sensors such as UAVs collect measurements to estimate the state of a moving target. Where the sensor goes determines how informative its measurements are, so its trajectory should account for the uncertainty in the estimate, not only its own dynamics and constraints.</p>
    <p>We formulate an estimation-aware optimal control problem that couples the nonlinear dynamics of the sensor and the target, the covariance dynamics of an extended Kalman filter, and nonlinear measurement models. The sensor's constraints hold in continuous time, even with sparse time discretization.</p>
  </div>

  <div class="project-results">
    <div class="project-block">
      <p class="project-kicker">Trading energy for information</p>
      <p>When the objective weights estimation uncertainty, the UAV maneuvers toward the ground vehicle to collect more informative measurements before reaching its final position. The ellipse shows the uncertainty in the target's estimated position.</p>
      <div class="project-gallery">
        <figure class="project-visual">
          <img src="{{ '/images/projects/eac_tracking_1.gif' | relative_url }}" alt="UAV flying directly to its final position while tracking a ground vehicle">
          <figcaption>Energy-only weighting: the UAV flies directly to its final position (star)</figcaption>
        </figure>
        <figure class="project-visual">
          <img src="{{ '/images/projects/eac_tracking_2.gif' | relative_url }}" alt="UAV maneuvering toward a ground vehicle to reduce estimation uncertainty">
          <figcaption>Covariance-only weighting: the UAV moves toward the ground vehicle to reduce estimation uncertainty</figcaption>
        </figure>
      </div>
    </div>

    <div class="project-block">
      <p class="project-kicker">Continuous-time constraint satisfaction</p>
      <p>A discretized benchmark can violate the sensor's constraints between discretization points. Our method satisfies them along the entire trajectory.</p>
      <ul class="project-facts">
        <li><strong>Application</strong><span>UAV tracking of a ground vehicle and localization of an LTE transmitter.</span></li>
      </ul>
      <p class="project-actions">
        <a class="project-action" href="https://arxiv.org/abs/2610.06654">arXiv 2026 paper</a>
      </p>
    </div>
  </div>
</section>

<section class="project-section" id="uav-ugv-energy-sharing">
  <div class="project-head">
    <span class="project-number">03</span>
    <div>
      <h2>Trajectory Optimization for Energy-Sharing UAV-UGV Systems</h2>
      <p class="project-subtitle">A ground vehicle serves as a mobile charging station, extending how long a UAV can operate.</p>
    </div>
  </div>

  <div class="project-overview">
    <p>Pairing a UAV with a UGV that serves as a mobile charging station keeps the UAV operational longer in areas with little infrastructure. Planning for such a team is hard: the UGV can only travel on certain terrain, and deciding which task locations to visit and when is a discrete scheduling problem.</p>
    <p>We formulate a smooth nonlinear program that jointly optimizes the trajectories of the UAV and the UGV. It models the UGV's terrain access constraints smoothly, allows partial recharging, and approximates the discrete scheduling logic with smooth constraints. As a result, standard nonlinear programming algorithms can solve it without integer variables.</p>
  </div>

  <div class="project-results">
    <div class="project-showcase">
      <div class="project-showcase-copy">
        <p class="project-kicker">No integer variables</p>
        <p>Compared with mixed-integer nonlinear programming, our model reduces computation time by orders of magnitude.</p>
        <ul class="project-facts">
          <li><strong>Application</strong><span>A UAV and a UGV visiting multiple task locations.</span></li>
        </ul>
        <p class="project-actions">
          <a class="project-action" href="https://arxiv.org/abs/2603.28447">arXiv 2026 paper</a>
        </p>
      </div>
      <figure class="project-visual">
        <img src="{{ '/images/projects/uav_ugv_energy_sharing.gif' | relative_url }}" alt="A UGV driving along a path network while a UAV visits task locations">
        <figcaption>The UGV travels along accessible paths (blue) while the UAV visits task locations (asterisks), which turn black once visited</figcaption>
      </figure>
    </div>
  </div>
</section>

<section class="project-section" id="uav-mobile-charging">
  <div class="project-head">
    <span class="project-number">04</span>
    <div>
      <h2>Trajectory Optimization for UAVs with Mobile Charging Support</h2>
      <p class="project-subtitle">Deciding when and where a UAV recharges on a mobile charging station while completing its tasks.</p>
    </div>
  </div>

  <div class="project-overview">
    <p>Mobile charging stations, such as ground vehicles that carry a charger, can extend a UAV's endurance in areas with little infrastructure. Planning such a mission couples task scheduling with decisions about when and where to recharge, and terrain limits where the charging station can go.</p>
    <p>We propose a smooth nonlinear trajectory optimization model with unified battery dynamics that capture nonlinear charging. We replace the disjunctive constraints on the time spent in each operating mode with smooth approximations that have bounded error, so the model has no integer variables and standard nonlinear optimization algorithms can solve it.</p>
  </div>

  <div class="project-results">
    <div class="project-showcase">
      <div class="project-showcase-copy">
        <p class="project-kicker">Charging on the move</p>
        <p>Compared with mixed-integer nonlinear programming, our model finds high-quality solutions while reducing computation time by orders of magnitude.</p>
        <ul class="project-facts">
          <li><strong>Application</strong><span>UAV missions with distributed tasks, nonlinear charging, and terrain-limited charging regions.</span></li>
        </ul>
        <p class="project-actions">
          <a class="project-action" href="https://arxiv.org/abs/2609.40201">arXiv 2026 paper</a>
        </p>
      </div>
      <figure class="project-visual">
        <img src="{{ '/images/projects/uav_mobile_charging.gif' | relative_url }}" alt="A UAV visiting task locations and recharging on a ground vehicle inside charging regions">
        <figcaption>The UAV visits task locations (asterisks) and recharges on a mobile charging station (blue dashed segments) inside the charging regions (gray)</figcaption>
      </figure>
    </div>
  </div>
</section>

<section class="project-section" id="uav-multiple-task-positions">
  <div class="project-head">
    <span class="project-number">05</span>
    <div>
      <h2>Nonlinear Trajectory Optimization for UAVs with Multiple Task Positions</h2>
      <p class="project-subtitle">Details coming soon.</p>
    </div>
  </div>
</section>

<section class="project-section" id="robot-platforms">
  <div class="project-head">
    <span class="project-number">06</span>
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
