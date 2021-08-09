# ubiquity workflow

## stage one

> set dbconfig key-value

```

for filteredCommand in filterCommands
do 
    exec fileterCommand
done

```

## stage two

> install os

```
if finished_step == 'ubiquity.components.partman_commit':
    begin intall
fi
```

## stage threee

> intall plugins

```
for plugin in plugins
do
    exec plugin
done
```

# package setup plugin

## contents
i. pageGTK
    > frontend - commuicate with user

2. page
    > filteredcommand - set dbconfig key-value through dbconfmodule

3. install
    > install plugin - get dbconfig key-value and setup package


# change log

1. v0.01
    > frame is done, include page and install plugin; working on UI.