simple_approach_planner:
  ros__parameters:
    disable_motion_planning: false
    planning_groups: # Sorted by order of preference
@[if has_arm]@
      - arm_torso
      - arm
@[else]@
      - torso
@[end if]@
    exclude_from_planning_joints:
      - head_1_joint
      - head_2_joint
@[if end_effector == "pal-hey5"]@
      - hand_thumb_joint
      - hand_mrl_joint
      - hand_index_joint
@[end if]@
@[if end_effector == "pal-gripper"]@
      - gripper_left_finger_joint
      - gripper_right_finger_joint
@[end if]@
    joint_tolerance: 0.01
    approach_velocity: 0.5
    approach_min_duration: 0.5
