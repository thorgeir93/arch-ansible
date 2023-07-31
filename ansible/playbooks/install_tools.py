---
- name: Install tools for Arch
  hosts: localhost
  become: yes

  vars:
    ansible_user: thorgeir

  tasks:
    - name: Install TMUX package
      pacman:
        name:
            - tmux
            - libfido2
        state: present
    # (optional) libfido2 needed for ssh-add command.

    - name: Desktop appearance
      pacman:
        name:
            - feh
            - picom
            - light
            - noto-fonts-emoji
            - powerline-fonts
        state: present

    - name: Audio
      pacman:
        name:
            - pipewire
            - pavucontrol
        state: present

    - name: Utils
      pacman:
        name:
            - tree
            - tk
            - rsync
        state: present
    # tk: for $ pyenv install 3.10.10

    - name: Add user to video group
      user:
        name: "{{ ansible_user }}"
        groups: video
        append: yes
    # Allow the user to use the light command.
