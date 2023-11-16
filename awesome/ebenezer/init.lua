local spawn = require("awful.spawn")
local envs = require("ebenezer.envs")

local function prepare_command(template_command)
    local command = template_command:gsub("{THEME_PATH}", envs.theme_path)

    return command
end

local function startup()
    if not envs.startup then return end

    for _, command in pairs(envs.startup) do
        spawn.with_shell(prepare_command(command))
    end
end


return { startup = startup }
