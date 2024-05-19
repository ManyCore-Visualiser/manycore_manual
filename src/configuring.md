# Configuring a Render

## State attributes configuration

State attributes can be configured from the `Settings`
menu, accessible via the gear icon in the bottom left. The menu allows
to select which attributes to display and how they should be displayed.
The following modalities are available for state attributes:

<table>
    <thead>
    <tr>
        <th rowspan="2">Attribute type</th>
        <th colspan="3">Target Element</th>
    </tr>
    <tr>
        <th>Core</th>
        <th>Router</th>
        <th>Channel</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td>Numerical</td>
        <td>
            <span class="emoji">&#x1F7EA;</span>
            <span class="emoji">&#128998;</span>
            <span class="emoji">&#128999;</span>
            <span class="emoji">&#129001;</span>
        </td>
        <td>
            <span class="emoji">&#x1F7EA;</span>
            <span class="emoji">&#128998;</span>
            <span class="emoji">&#128999;</span>
            <span class="emoji">&#129001;</span>
        </td>
        <td>
            <span class="emoji">&#128998;</span>
            <span class="emoji">&#128999;</span>
            <span class="emoji">&#129001;</span>
        </td>
    </tr>
    <tr>
        <td>String</td>
        <td>
            <span class="emoji">&#128999;</span>
            <span class="emoji">&#129001;</span>
        </td>
        <td>
            <span class="emoji">&#128999;</span>
            <span class="emoji">&#129001;</span>
        </td>
        <td>
            <span class="emoji">&#128999;</span>
            <span class="emoji">&#129001;</span>
        </td>
    </tr>
    </tbody>
</table>

Table legend:

- <span class="emoji">&#x1F7EA;</span> Element's body fill colour.
- <span class="emoji">&#128998;</span> Coloured text.
- <span class="emoji">&#128999;</span> Text.
- <span class="emoji">&#129001;</span> Statically coloured text (does not adapt to
numerical value, if any).

### Configuration how-tos

- [Text](./configuring/text.md)
- [Statically coloured text](./configuring/static_text.md)
- [Element's body fill colour](./configuring/fill.md)
- [Coloured text](./configuring/coloured_text.md)

## Further configuration

Other than the elements' attributes, other visualisation parameters can be customised.
These are:

- Text used to represent an attribute (showed in [Coloured text](./configuring/coloured_text.md)
by clicking on the
<svg xmlns="http://www.w3.org/2000/svg" height="1.5rem" viewBox="0 -960 960 960"
    width="1.5rem" fill="currentcolor">
    <path d="M280-160v-520H80v-120h520v120H400v520H280Zm360 0v-320H520v-120h360v120H760v320H640Z"/>
</svg> icon)
- [Attributes and Tasks font size](./configuring/font.md)
- [Whether to include border routers](./configuring/border_routers.md)
- [Routing algorithm and its representation modality](./configuring/routing.md)
- [Whether to include Task computation cost](./configuring/task.md)
- [Override fill colour](./configuring/override.md)
