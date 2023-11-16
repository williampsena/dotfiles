function run()
    collectgarbage("setpause", 110)
    collectgarbage("setstepmul", 1000)
end

return {run = run}
