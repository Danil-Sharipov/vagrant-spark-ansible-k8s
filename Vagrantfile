IMAGE_NAME = "bento/ubuntu-20.04"
N = 2

Vagrant.configure("2") do |config|
    config.ssh.insert_key = false
    config.vm.synced_folder '.', '/vagrant', disabled: true

    config.vm.provider "virtualbox" do |v|
        v.memory = 2048
        v.cpus = 2
    end
      
    config.vm.define "k8s-master" do |master|
        master.vm.box = IMAGE_NAME
        master.vm.network "private_network", ip: "192.168.56.10"
        master.vm.hostname = "k8s-master"
        # port-forward testing  
#         master.vm.network "forwarded_port", guest: 7077, guest_ip: "127.0.0.1", host: 7077, host_ip: "127.0.0.1", auto_correct: true
#         master.vm.network "forwarded_port", guest: 6443, guest_ip: "127.0.0.1", host: 6443, host_ip: "127.0.0.1", auto_correct: true
#         master.vm.network "forwarded_port", guest: 10051, guest_ip: "127.0.0.1", host: 10051, host_ip: "127.0.0.1", auto_correct: true
#         master.vm.network "forwarded_port", guest: 10050, guest_ip: "127.0.0.1", host: 10050, host_ip: "127.0.0.1", auto_correct: true
#         master.vm.network "forwarded_port", guest: 8080, guest_ip: "127.0.0.1", host: 8081, host_ip: "127.0.0.1", auto_correct: true
        # ssh -L 12345:localhost:6443 vagrant@172.26.64.1 -p 2222
    end

    (1..N).each do |i|
        config.vm.define "node-#{i}" do |node|
            node.vm.box = IMAGE_NAME
            node.vm.network "private_network", ip: "192.168.56.#{i + 10}"
            # private_network
            node.vm.hostname = "node-#{i}"
            # node.vm.provision "ansible" do |ansible|
            #     ansible.playbook = "kubernetes-setup/node-playbook.yml"
            # end
        end
    end
end
