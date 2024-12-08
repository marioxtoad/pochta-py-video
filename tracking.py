from config import token, password
from pochta.tracking import SingleTracker

tracking = SingleTracker(token, password)

history = tracking.get_history("80093403330917")
print(history[2])
