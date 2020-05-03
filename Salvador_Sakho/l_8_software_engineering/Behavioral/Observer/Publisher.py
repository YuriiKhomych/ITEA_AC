from collections import defaultdict
from copy import deepcopy
import smtplib
from email.message import EmailMessage


class Publisher:
    def __init__(self, factories_list):
        self._old_factories_list = deepcopy(factories_list)
        self._current_factories_list = factories_list
        self._subscriptions = defaultdict(list)
        self.old_factory_product = [
            factories.available_robots for
            factories in self._old_factories_list][0]
        self.current_factory_product = [
            factories.available_robots for
            factories in self._current_factories_list][0]

    def __subscribe(self, subscriber_name, observable_entities):
        for entity in self._old_factories_list:
            if observable_entities == entity.__class__.__name__:
                self._subscriptions[observable_entities].append(
                    subscriber_name
                )
                return 'You was subscribed!'
        return 'No such observable object'

    def __unsubscribe(self, subscriber_name, observable_entities):
        if subscriber_name not in self._subscriptions[observable_entities]:
            return 'No such subscriber'
        for entity in self._old_factories_list:
            if observable_entities in entity.__class__.__name__:
                self._subscriptions[observable_entities].remove(
                    subscriber_name)
                return 'You was un subscribed!'
        return 'No such observable object'

    def check_for_update(self, observable_entities, subscriber_name=''):
        if observable_entities not in self.current_factory_product \
                and observable_entities not in self.old_factory_product:
            if len(self.current_factory_product) \
                    != len(self.old_factory_product):
                # если subscriber_name не пуст то отправляет обновления
                # подписчику, иначе отправляем обновления всем подписчикам
                if subscriber_name in self._subscriptions[observable_entities]:
                    return self._notify_subscriber(
                        subscriber_name, observable_entities
                    )
                else:
                    return self._notify_subscriber(
                        self._subscriptions[observable_entities],
                        observable_entities
                    )
            return f'There are no changes in: {observable_entities}'
        return 'No such observable entities'

    def _notify_subscriber(self, subscribers_name, observable_entities):
        observable_entities_name = observable_entities \
            if isinstance(observable_entities, str) \
            else observable_entities.__class__.__name__
        data_for_send = [
            factories.available_robots
            for factories in self._current_factories_list if
            observable_entities_name == factories.__class__.__name__
        ][0]
        msg = EmailMessage()
        msg.set_content(str(data_for_send))
        msg['Subject'] = f'The contents of {str(data_for_send)}'
        msg['From'] = f'testEmail@gmial.com'
        subscribers = subscribers_name \
            if isinstance(subscribers_name, str) == 1 \
            else ', '.join(subscribers_name)
        msg['To'] = subscribers
        with smtplib.SMTP('localhost') as s:
            s.send_message(msg)
        return 'Notifications where sent to subscribers  email'

    def api(self, subscriber_request):
        return {
            'subscribe': self.__subscribe,
            'unsubscribe': self.__unsubscribe,
            'get updates': self.check_for_update,
        }.get(subscriber_request['command'],
              lambda **kwargs: 'No such command')(
            subscriber_request['email'],
            subscriber_request['observable object'],
        )
