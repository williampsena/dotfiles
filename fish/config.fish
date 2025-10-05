set fish_greeting

if test -f $HOME/.profile
    for line in (bash -c "source $HOME/.profile >/dev/null 2>&1; env" | grep -v '^BASH_FUNC_')
        set -l name (echo $line | cut -d= -f1)
        set -l value (echo $line | cut -d= -f2-)
        
        if contains $name PWD SHLVL _ 
            continue
        end
        
        set -x $name $value
    end
end

if status is-interactive
    starship init fish | source
end

mise activate fish | source
