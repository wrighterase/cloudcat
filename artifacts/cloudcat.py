#!/usr/bin/python3
#import ansible_runner
#import os
#cwd = os.getcwd()
#ansible_runner.run(playbook=cwd + '/test-yaml.yml', cmdline='--vault-id @prompt', extravars={'foo':'one','bar':'two','baz':'three'})
#
#!/usr/bin/python3
#import ansible_runner
#r = ansible_runner.run(private_data_dir='/tmp/demo', playbook='/home/user/dev/cloudcat/creation.yml')
#print("{}: {}".format(r.status, r.rc))
# successful: 0
#for each_host_event in r.events:
#    print(each_host_event['event'])
#print("Final status:")
#print(r.stats)

if __name__ == "__main__":
    banner()
    main()
