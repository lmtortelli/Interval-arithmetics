import fenv

__all__ = [
    "Round"
]

class Round(object):

	@staticmethod
	def set_down_rounding():
		fenv.ROUND.set(fenv.ROUND.DOWNWARD)

	@staticmethod
	def set_up_rounding():
		fenv.ROUND.set(fenv.ROUND.UPWARD)

	@staticmethod
	def set_normal_rounding():
		fenv.ROUND.set(fenv.ROUND.TONEAREST)

	@staticmethod
	def get_rounding():
		return (fenv.ROUND.get())
