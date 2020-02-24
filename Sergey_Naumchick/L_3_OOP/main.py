from hw_start import insights
import baseinsight

for insight in insights:

    try:
        bi = baseinsight.BaseInsight(**insight)
        try:
            print(len(bi))
        except Exception:
            pass
    except KeyError as err:

        print(f"Error: {err}")

    else:
        print(bi.__dict__)
        print(bi.get_attribute_by_name("period"))
