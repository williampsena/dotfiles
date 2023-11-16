local function deepcopy_table(orig)
    local orig_type = type(orig)
    local copy
    if orig_type == 'table' then
        copy = {}
        for orig_key, orig_value in next, orig, nil do
            copy[deepcopy_table(orig_key)] = deepcopy_table(orig_value)
        end
        setmetatable(copy, deepcopy_table(getmetatable(orig)))
    else -- number, string, boolean, etc
        copy = orig
    end
    return copy
end

local function merge_tables(first_table, second_table)
    local merged_table = deepcopy_table(first_table)

    if not second_table then return merged_table end

    for k, v in pairs(second_table) do
        merged_table[k] = v
    end

    return merged_table
end

local function split(string_to_split, separator)
    if separator == nil then separator = "%s" end
    local parsed_table = {}

    for value in string.gmatch(string_to_split, "([^" .. separator .. "]+)") do
        table.insert(parsed_table, value)
    end

    return parsed_table
end

return { merge_tables = merge_tables, deepcopy_table = deepcopy_table, split = split }
