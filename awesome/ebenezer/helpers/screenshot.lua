local awful = require("awful")
local naughty = require("naughty")
local style = require('ebenezer.style')

local delay_timers = {5, 10}
local screenshot_dir = os.getenv("HOME") .. "/Pictures/Screenshots"
local screenshot_icon = ""

local function get_target_file()
    local filename = "Screenshot_from_" .. os.date("!%Y-%m-%d_%H-%M-%S") ..
                         ".png"

    return filename, screenshot_dir .. "/" .. filename
end

local function run_command(command, filename)
    awful.spawn.easy_async_with_shell(command,
                                      function(stdout, stderr, _reason,
                                               _exitcode)

        if string.find(stderr, "abort") then return end

        naughty.notify({
            title = screenshot_icon .. " Screenshot",
            font = style.font_strong,
            text = filename,
            position = 'top_right',
            bg = style.bg_focus,
            fg = style.fg_normal,
            margin = 10
        })
    end)
end

local function print_screen()
    local filename, filepath = get_target_file()

    run_command("scrot '" .. filepath ..
                    "' -e 'xclip -selection c -t image/png < $f'", filename)
end

local function print_screen_selection()
    local filename, _ = get_target_file()

    run_command("sleep 0.5 && scrot " .. filename .. " -s -e 'mv $f " ..
                    screenshot_dir .. "' | exit 0", filename)
end

local function print_screen_window()
    local filename, filepath = get_target_file()

    run_command("scrot -u " .. filepath ..
                    " -e 'xclip -selection c -t image/png < $f'", filename)
end

local function print_screen_delay()
    local delayed_screenshot = function(delay)
        return function()
            local filename, filepath = get_target_file()

            run_command("scrot -d " .. delay .. " " .. filepath ..
                            " -e 'xclip -selection c -t image/png < $f'",
                        filename)
        end

    end

    local items = {}

    for _, value in ipairs(delay_timers) do
        items[#items + 1] = {
            "  " .. tostring(value) .. " second delayed screenshot",
            delayed_screenshot(value)
        }
    end

    awful.menu.new({items = items, theme = {width = 300}}):show({
        keygrabber = true
    })
end

local function setup_keybindings()
    awful.keyboard.append_client_keybindings({
        awful.key({}, "Print", print_screen, {
            description = "Take a screenshot of entire screen",
            group = "screenshot"
        }), awful.key({modkey}, "Print", print_screen_selection, {
            description = "Take a screenshot of selection",
            group = "screenshot"
        }), awful.key({"Shift"}, "Print", print_screen_window, {
            description = "Take a screenshot of focused window",
            group = "screenshot"
        }), awful.key({"Ctrl"}, "Print", print_screen_delay, {
            description = "Take a screenshot of delay",
            group = "screenshot"
        })
    })
end

return {
    print_screen = print_screen,
    print_screen_delay = print_screen_delay,
    print_screen_selection = print_screen_selection,
    print_screen_window = print_screen_window,
    setup_keybindings = setup_keybindings
}
