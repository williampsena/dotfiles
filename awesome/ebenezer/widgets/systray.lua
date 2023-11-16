local wibox = require('wibox')
local style = require('ebenezer.style')

local function factory()
    local systray = wibox.widget {
        font = style.font_regular,
        widget = wibox.widget.systray
    }

    return wibox.container.margin(systray)
end

return factory
