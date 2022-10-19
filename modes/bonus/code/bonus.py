from mpf.core.mode import Mode
import asyncio

# Bonus mode trying to emulate what happens in the real EM machine
#   See Vid Camps Sure Shot clipped: https://youtube.com/clip/UgkxlNKh9j2blmnCA238TiZ1xtqN9AcK2sho
class Count(Mode):
    def mode_start(self, **kwargs):
        self.machine.events.post("bonus_mode_start")
        
        self.bonus_value = 1000
        self.count_down = self.player["total_balls_collected"]
        self.total_run = 0

        self.machine.events.post("bonus_start" + str(self.count_down))
        
        # Delay the calculation by 1s to simulate EM natural delay
        self.delay.add(1000, self.check_score_reels)

    def check_score_reels(self, **kwargs):
        self.machine.events.post("bonus_code_check_score_reels_valid")

        ready_future = asyncio.ensure_future(self.machine.score_reel_groups.srg_score.wait_for_ready(), loop=self.machine.clock.loop)
        ready_future.add_done_callback(self.bonus_step)

    def bonus_step(self, future=None, **kwargs):
        self.machine.events.post("bonus_code_step")

        # add a slight delay every 5k, to simulate what EM machine did
        delay = 0
        if (self.total_run > 0 and self.total_run % 5 == 0):
            delay = 150

        if self.count_down > 0:
            self.delay.add(ms=delay, callback=self.do_bonus_step)
        else:
            self.bonus_pause()
            
    def do_bonus_step(self):
        self.machine.events.post("bonus_code_countdown_" + str(self.count_down))
        self.player.score += self.bonus_value

        self.count_down -= 1
        self.total_run += 1
        self.check_score_reels()

    def bonus_pause(self):
        # pause for 1s to have a natural end of bonus
        self.delay.add(ms=1000, callback=self.bonus_done)

    def bonus_done(self):
        self.machine.events.post("bonus_complete")
        self.stop()
