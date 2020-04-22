from hw_start import insights
import BaseInsight
from Test import insight_builder

for insight in insights:

    try:
        bi = BaseInsight.BaseInsight(**insight)

    except KeyError as err:

        print(f"Error: {err}")

    else:
        print(bi.__dict__)

print()
print("NOW COPY:")
print()

insight_builder(insights)
