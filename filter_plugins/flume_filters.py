#!/usr/bin/env python3

class FilterModule(object):
    def filters(self):
        return {
            'flume_configuration': self.flume_configuration,
            'flume_sources': self.flume_sources,
            'flume_sinks': self.flume_sinks,
            'flume_channels': self.flume_channels,
            'flume_agents': self.flume_agents,
        }

    @staticmethod
    def extract_keys(data):
        keys = []
        if isinstance(data, dict):
            for key in data:
                keys.append(key)
        return keys

    def flume_configuration(self, data, agent=""):
        if agent != "":
            data = data[agent]
        return self.flume_configuration_internal(data)

    def flume_configuration_internal(self, data, path='', configuration={}):
        if not isinstance(data, dict):
            configuration[path[:-1]] = data
        else:
            for key in data:
                self.flume_configuration_internal(data[key], path + key + '.', configuration)
        return configuration

    def flume_elements(self, data, element, elements=[]):
        if isinstance(data, dict):
            for key in data:
                if key == element:
                    elements = elements + self.extract_keys(data[key])
                elements = self.flume_elements(data[key], element, elements)
        return elements

    def flume_sources(self, data, agent=""):
        if agent != "":
            data = data[agent]
        return self.flume_elements(data, "sources")

    def flume_sinks(self, data, agent=""):
        if agent != "":
            data = data[agent]
        return self.flume_elements(data, "sinks")

    def flume_channels(self, data, agent=""):
        if agent != "":
            data = data[agent]
        return self.flume_elements(data, "channels")

    def flume_agents(self, data):
        return self.extract_keys(data)
