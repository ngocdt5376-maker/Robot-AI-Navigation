import unittest
from robot_ai.domain.environment import Environment, MAPS
from robot_ai.domain.robot import Robot
from robot_ai.algorithms.search import WeightedAStar, WeightedAStarAgent, LRTAStarAgent
from robot_ai.application.simulation import Simulation

class EnvironmentTests(unittest.TestCase):
    def test_three_maps_have_start_and_goal(self):
        self.assertEqual(set(MAPS), {1, 2, 3})
        for map_id in MAPS:
            env = Environment(map_id)
            self.assertTrue(env.is_free(env.start))
            self.assertTrue(env.is_free(env.goal))

    def test_robot_observes_without_knowing_full_map(self):
        env = Environment(1)
        robot = Robot(env)
        self.assertEqual(robot.known, {})
        robot.observe(env)
        self.assertGreater(len(robot.known), 0)
        self.assertLess(len(robot.known), env.rows * env.cols)

class AlgorithmTests(unittest.TestCase):
    def test_weighted_astar_finds_path_on_open_grid(self):
        passable = lambda p: 0 <= p[0] < 3 and 0 <= p[1] < 3
        path, expanded = WeightedAStar(1.5).search(passable, (0, 0), (2, 2))
        self.assertEqual(path[0], (0, 0))
        self.assertEqual(path[-1], (2, 2))
        self.assertEqual(len(path) - 1, 4)
        self.assertGreater(expanded, 0)

    def test_both_agents_can_decide(self):
        env = Environment(1)
        robot = Robot(env)
        robot.observe(env)
        for agent in (WeightedAStarAgent(), LRTAStarAgent()):
            nxt, message = agent.decide(robot)
            self.assertIsNotNone(nxt)
            self.assertTrue(env.in_bounds(nxt))
            self.assertIsInstance(message, str)

class SimulationTests(unittest.TestCase):
    def test_step_never_enters_wall_or_outside(self):
        sim = Simulation(map_id=1, algorithm="astar")
        for _ in range(100):
            if sim.finished:
                break
            before = sim.robot.pos
            sim.step()
            if sim.robot.pos != before:
                self.assertTrue(sim.env.is_free(sim.robot.pos))
        self.assertLessEqual(sim.robot.steps, 100)

    def test_reset_restores_start_state(self):
        sim = Simulation(map_id=1, algorithm="lrta")
        sim.step()
        sim.reset()
        self.assertEqual(sim.robot.pos, sim.env.start)
        self.assertEqual(sim.robot.steps, 0)
        self.assertEqual(sim.robot.status, "Chưa bắt đầu")

    def test_all_six_map_algorithm_runs_reach_goal(self):
        for map_id in (1, 2, 3):
            for algorithm in ("astar", "lrta"):
                with self.subTest(map_id=map_id, algorithm=algorithm):
                    sim = Simulation(map_id=map_id, algorithm=algorithm)
                    sim.run_to_end()
                    self.assertTrue(sim.stats()["success"])
                    self.assertEqual(sim.robot.pos, sim.env.goal)

if __name__ == "__main__":
    unittest.main()
