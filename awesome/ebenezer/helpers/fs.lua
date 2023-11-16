function file_exists(file_path)
    local file = io.open(file_path, "r")
    return file ~= nil and io.close(file)
end

function resolve_path(relative_path, path_vars)
    return string.gsub(relative_path, "%$(%w+)", path_vars)
end

local function get_files(directory)
    local i, files, popen = 0, {}, io.popen

    for filename in popen([[find "]] .. directory .. [[" -type f]]):lines() do
        i = i + 1
        files[i] = filename
    end

    return files
end

return {
    file_exists = file_exists,
    resolve_path = resolve_path,
    get_files = get_files
}
