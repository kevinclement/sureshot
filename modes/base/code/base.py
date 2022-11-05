from mpf.core.mode import Mode

# Class used as a simple place to test code-behind temporarily
class Playground(Mode):

    def mode_start(self, **kwargs):
        self.log.info("Base Playground Mode Running...")