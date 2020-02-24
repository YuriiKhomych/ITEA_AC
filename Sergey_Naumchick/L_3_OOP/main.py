from hw_start import insights
import baseinsight

for insight in insights:

    try:
        bi = baseinsight.BaseInsight(**insight)

    except KeyError as err:

        print(f"Error: {err}")

    else:
        print(bi.__dict__)
