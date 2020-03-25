from hw_start import insights


def summary(insights):
    if isinstance(insights, dict):
        for key, value in insights.items():

            try:

                if key == 'period' and value > 4:
                    insights[key] = 7
                elif key == 'period' and value is None:
                    insights[key] = 7

                if key == 'metric_sums':
                    for val in value:
                        if val['sum_general'] != 0:

                            if insights['api'] == 1:
                                val[
                                    'summary'] = (val['sum'] * val['sum_level']
                                                  / val['sum_general']) / insights['period']
                            elif insights['api'] == 2:
                                val[
                                    'summary'] = (val['sum'] * val['sum_level'] ** 2
                                                  / val['sum_general']) / insights['period']
                            elif insights['api'] == 3:
                                val[
                                    'summary'] = (val['sum_level'] / val['sum_general']) / insights['period']
                            elif insights['api'] == 4:
                                val['summary'] = f"{(val['sum_level'] * 100) / insights['period']}"

                if key == "metric_sums":
                    for values in value:
                        if values["sum_general"] != 0:

                            if insights["api"] == 1:
                                values[
                                    "summary"
                                ] = (values['sum'] * values['sum_level']
                                     / values['sum_general']) / insights['period']
                            elif insights["api"] == 2:
                                values[
                                    "summary"
                                ] = (values['sum'] * values['sum_level'] ** 2
                                     / values['sum_general']) / insights['period']
                            elif insights["api"] == 3:
                                values[
                                    "summary"
                                ] = f"{(values['sum_level'] / values['sum_general']) / insights['period']}"
                            elif insights["api"] == 4:
                                values[
                                    "summary"
                                ] = f"{(values['sum_level'] * 100) / insights['period']}"

                            if insights['api'] == 1:
                                values['summary'] = \
                                    (values['sum'] * values['sum_level'] / values['sum_general']) / insights['period']
                            elif insights['api'] == 2:
                                values[
                                    'summary'] = (values['sum'] * values['sum_level'] ** 2
                                                  / values['sum_general']) / insights['period']
                            elif insights['api'] == 3:
                                values[
                                    'summary'] = (values['sum_level'] / values['sum_general']) / insights['period']
                            elif insights['api'] == 4:
                                values['summary'] = f"{(values['sum_level'] * 100) / insights['period']}"

                            else:
                                values["summary"] = "Zero division problem!"

                        return print(values)
            except Exception as error:
                print(f'Houston we have {error}')

    elif isinstance(insights, list):
        for insight in insights:
            summary(insight)


summary(insights)
