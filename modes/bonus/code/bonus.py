from mpf.core.mode import Mode
from mpf.core.delays import DelayManager
from mpf.core.utility_functions import Util

class Count(Mode):
    def mode_start(self, **kwargs):
        self.machine.events.post("bonus_mode_start")
        # if self.player['ball'] == 3:
        #    self.bonus_value = 2000
        # else:
        #    self.bonus_value = 1000

        # self.count_down = self.machine.counters.lb_bonus.value
        # self.machine.events.post("bonus_start" + str(self.count_down))
        self.prepare_bonus()

    def prepare_bonus(self):
        self.machine.events.post("prepare_bonus")
        # self.machine.events.post('stop_bonus_shows')

        # for loop in range(1000, self.count_down + 1000, 1000):
        #     self.machine.lights['pfl_bonus_' + str(loop)].on()

        self.check_score_reels()

    def check_score_reels(self, **kwargs):
        self.machine.events.post("bonus_code_check_score_reels_valid")

        # TMP: TODO: REMOVE
        self.bonus_step()

        # if self.player['player_number'] == 1:
        #     ready_future = Util.ensure_future(self.machine.score_reel_groups.player1.wait_for_ready(), loop=self.machine.clock.loop)
        # else:
        #     ready_future = Util.ensure_future(self.machine.score_reel_groups.player2.wait_for_ready(), loop=self.machine.clock.loop)

        # ready_future.add_done_callback(self.bonus_step)

    def bonus_step(self, future=None, **kwargs):
        self.machine.events.post("bonus_code_step")

        # TMP: TODO: REMOVE
        self.bonus_pause()

        # if self.count_down > 0:
        #     self.delay.add(ms=500, callback=self.do_bonus_step)
        # else:
        #     self.bonus_pause()
            
    def do_bonus_step(self):
        self.machine.events.post("do_bonus_step")
        # self.machine.events.post("bonus_code_countdown_" + str(self.count_down))
        # self.player.score += self.bonus_value

        # self.machine.shows['flash'].play(show_tokens=dict(light='pfl_bonus_' + str(self.count_down)), speed=10.0, loops=3)
        # self.machine.lights['pfl_bonus_' + str(self.count_down)].off()

        # self.count_down -= 1000

        # self.check_score_reels()

    def bonus_pause(self):
        self.machine.events.post("bonus_pause")
        self.delay.add(ms=1000, callback=self.bonus_done)

    def bonus_done(self):
        self.machine.events.post("bonus_complete")
        self.stop()
