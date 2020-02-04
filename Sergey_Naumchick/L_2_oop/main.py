from hw_start import insights
import BaseInsight

for insight in insights:


    try:
        bi = BaseInsight.BaseInsight(**insight)

    except KeyError as err:

        print(f"Error: {err}")

    else:
        print(bi.__dict__)

