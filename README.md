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
1. pageGTK
    > frontend - commuicate with user

2. page
    > filteredcommand - set dbconfig key-value through dbconfmodule

3. install
    > install plugin - get dbconfig key-value and setup package


# change log

1. v0.01
    > frame is done, include page and install plugin; working on UI.

2. v0.02
    > UI is done， begin to debug.

3. v0.03
    > debug is done, install plugin not verify.

4. v0.04
    > add hook.

5. v0.05
    > fix error.

6. v0.06
    > add cleanup method.

7. v0.07
    > add log
    > change plugin index

8. v0.08
    >fix bugs
