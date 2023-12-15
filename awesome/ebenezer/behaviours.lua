require("awful.autofocus")

function setup(client)
    -- Focus clients under mouse
    client.connect_signal("mouse::enter", function(c)
        c:emit_signal("request::activate", "mouse_enter", {raise = false})
    end)
end

return {setup = setup}
