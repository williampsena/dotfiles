function file_exists(file_path)
    local file = io.open(file_path, "r")
    return file ~= nil and io.close(file)
end

return {file_exists = file_exists}
