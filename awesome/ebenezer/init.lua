local spawn = require("awful.spawn")
local envs = require("ebenezer.envs")
local fs = require('ebenezer.helpers.fs')
local function prepare_command(template_command)
    return fs.resolve_path(template_command, envs.path_vars)
end

local function startup()
    if not envs.startup then return end

    for _, command in pairs(envs.startup) do
        spawn.with_shell(prepare_command(command))
    end
end


return { startup = startup }
