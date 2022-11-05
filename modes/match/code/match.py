import asyncio

from mpf.core.async_mode import AsyncMode
from random import *

class Match(AsyncMode):
    @asyncio.coroutine
    def _run(self):
        self.player_matches = [False, False, False, False]
        self.match_numbers  = ['00', '10', '20', '30', '40', '50', '60', '70', '80', '90']
        aMatchFound = False

        # make sure all match lights are off
        for loop in self.match_numbers:
            self.machine.lights["bbl_match_" + loop].off(key="match")

        # calculate the winning random number, and turn its light on
        self.log.info("Calculating random winning match number...")
        random_match_numbers = self.match_numbers
        shuffle(random_match_numbers)
        self.match = random_match_numbers[0]
        self.match_light = "bbl_match_" + self.match
        self.log.info(f'MATCH found was {self.match} and light {self.match_light}')

        # pull out the players scores and their match numbers
        player_list = self.machine.game.player_list
        for i in range(0, len(player_list), 1):
            p_score = player_list[i].score
            p_num = i + 1
            self.log.info(f'Player {p_num} score: {str(p_score)}')
            match_score = '{:02}'.format(int(str(int(str(p_score)[-2:]))[-2:1]) * 10)
            self.log.info(f'Player {p_num} Match Score: {str(match_score)}')

            if (self.match == match_score):
                self.log.info(f'Player {p_num} MATCHED!!!!')
                self.player_matches[i] = True
                aMatchFound = True

        # just turn on the match lamp
        self.machine.lights[self.match_light].on(key="match")

        # if we found a match, then lets blink the match number
        if aMatchFound: 
            self.machine.shows['flash'].play(
                show_tokens=dict(leds=self.match_light))

        # fire knocker for each match
        for i in range(0, len(player_list), 1):
            if self.player_matches[i]:
                self.machine.shows['match_knocker'].play(loops=0)

        self.machine.events.post('match_code_ended')