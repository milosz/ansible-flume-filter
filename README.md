# ansible-flume-filter
https://sleeplessbeastie.eu/2021/06/04/how-to-create-ansible-filters/

Apache Flume filters:
  * `flume_agents`
    extract agents
  * `flume_sources`
    extract sources, may be limited to a specific agent
  * `flume_sinks`
    extract sinks, may be limited to a specific agent
  * `flume_channels`
    extract channels, may be limited to a specific agent
  * `flume_configuration`
    extract configuration rules, may be limited to a specific agent

Edit `filter_plugins/flume_filters.py` file to edit filters.

Sample configuration.
```yaml
agent:
  sources:
    seqGenSrc:
      type: seq
      channels: memoryChannel
  channels:
    memoryChannel:
      type: memory
      capacity: 100
  sinks:
    loggerSink:
      type: logger
      channel: memoryChannel
```

Test `template.j2` template.

```shell
$ ansible-playbook playbook.yml
```
