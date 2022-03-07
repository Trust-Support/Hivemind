***
PART 1
SKY BASICS
-----
Hello! Thanks for purchasing Ultra Dynamic Sky!
This short readme should cover all the basics, but if you have any questions or run into any problems, please email me at everettgunther@gmail.com
Also, there are tooltips for just about every setting on the sky and weather, so if you're confused about what something does, hover over it for a specific explanation.
-----
ADDING THE SKY TO YOUR SCENE
-----
First make sure you delete from your scene any existing lights for the sun, moon, and skylight, as well as any existing fog actors, sky spheres, or sky atmosphere actors.
If after doing this there is still some ambient light present, that probably means there's still static light in the lightmaps from the previous lighting solution, so run a lighting build (from the Build dropdown on the main toolbar) to clear that out.
Drag the Ultra_Dynamic_Sky actor into your scene from the Blueprints folder.
The default state of the sky will use the built in light components for the sun, moon and sky light, and all three will be movable by default. If you need to, you can adjust their mobility using the settings in the Component Selection and Mobility category.
-----
SETTING THE TIME OF DAY
-----
Change the Time of Day property in Basic Controls to adjust the time of day the system will start with. If you need more control over the path of the Sun, you can also adjust Sun Angle and Sun Inclination in the Sun category.
The Time of Day variable is a single float from 0 to 2400. This is to simplify things like setting and animating the time. But if you need, you can access the Time at runtime as an Hours/Minutes/Seconds value using the "Get Time of Day in Real Time Format" function or as a DateTime structure using "Get Current Date and Time".
If you want to adjust the specific times that the sun comes up and goes down, you can do that with the Dawn Time and Dusk Time settings, also in Basic Controls. For setting up a realistic sun based on world coordinates, see the section below about the Simulation category.
-----
SETTING THE SKY MODE
-----
In Basic Controls, there is a setting called Sky Mode. This controls some fundamental things. Specifically the type of dynamic clouds and whether or not the system uses the Sky Atmosphere for coloring. Here is a quick explanation of each option:>1. Volumetric Clouds - Enabled by default, this sky mode uses a field of full 3D volumetric clouds. This can offer
 the most realistic visuals, but at a performance cost that may be too much for some projects/platforms.
2. Static Clouds - Designed to mimic the look of the volumetric clouds but as a static cloud texture. Much lower performance cost than volumetric clouds. Incompatible with aurora effects. This mode does its best to adapt to cloud density so it can still be used with weather effects, but the cloud formations being static makes those transitions much less natu
ral looking.
3. 2D Dynamic Clouds - Dynamic clouds drawn using panning 2D textures.
4. No Clouds - This mode uses no dynamic clouds at all.
5. 2D Clouds using Color Curves - The 2D Clouds, but paired with UDS's old solution for color. This utilizes color curves to determine all of the colors which make up the sky. Often not as realistic as sky atmosphere, but it has the benefit of a lighter performance cost and is totally customizable by editing the curves in the Legacy Color category.
6. Volumetric Aurora - Sacrifices clouds to render full 3D aurora effects. Adjustable using the settings in the Aurora category.If you decide to use Volumetric Clouds, also take note of the setting called Volumetric Cloud Rendering Mode, in the Volumetric Clouds category. It determines how the volumetric clouds are rendered and has a large impact on performa
nce and quality. It also determines if volumetric clouds can render over opaque objects.
-----
ADJUSTING THE CLOUDS
-----
In the Basic Controls category, you can make adjustments to the cloudiness using the Cloud Coverage property.
In the Volumetric Clouds category, you can adjust settings for the 3D Volumetric Clouds. Some key things adjustable here include the altitude of the clouds, their scale, and their density.
In the 2D Dynamic Clouds category, you'll find all the settings relating to the look of the 2D clouds, from softness and shading effects to the noise texture used to generate the clouds.
In the Cloud Movement category, you can change the clouds' speed as they move across the sky. You can set the Cloud Speed variable to 0 if you want the clouds to be static. To adjust the formation of static clouds, you can use the Cloud Phase property. Note that if you have UDW also placed in your scene, the cloud speed will be controlled from there, using t
he current wind speed/direction, so it will not be editable on UDS.
In Cloud Shadows, you can also enable and disable the cloud shadows cast by the sun and moon. It's highly recommended to leave this enabled. You can also adjust how soft cloud shadows are and how intensely they darken the light.
-----
ADJUSTING THE SKY ATMOSPHERE SETTINGS
-----
The Sky Atmosphere is what determines the coloring of the sky, by default.
UDS by default will control some of these atmosphere settings based on current cloud coverage. You can adjust how/if it controls these settings from the Sky Atmosphere category on UDS.
To directly control all of the sky atmosphere settings yourself, look to the component list at the top of the details panel for UltraDynamicSky. Find the "SkyAtmosphere" component and select it. You should now see all of the settings for the component. The settings categories labeled "Atmosphere" are the most relevant ones for adjusting the look of the sky.
-----
ADJUSTING THE MOON AND STARS
-----
You can adjust the Moon in several ways in the Moon category. You can change its scale in the sky, its inclination and angle (the path it takes across the sky), its color, and its intensity. You can also adjust the moon's phase, from 0 to 27.
The Moon category also contains settings for the moon's directional light. It's color, intensity, and if it casts shadows.
In the Stars category you can change the intensity of the stars, when they appear at night, the speed they move, and their color.
From these categories you can also select your own custom texture for the moon or the stars.
-----
SETTING UP A DAY/NIGHT CYCLE
-----
In the Animate Time of Day category, check the box labelled Animate Time of Day. When you play the game, the sky will animate indefinitely, starting at the time of day you have  selected. You can change the Day Length and Night Length as well, which is entered in a value of minutes.
Note that time will only move forward if you have Movable selected for the Sun's mobility.
If you have Simulate Real Sun enabled in the Simulation category, the speed time moves is determined by Simulation Speed, not Day Length and Night Length.
-----
CONFIGURING THE SKY LIGHT
-----
In the Sky Light category, Sky Light Mode determines the source for the sky light cube map. There are three options:>1. Capture Based: The sky light will generate a cubemap by capturing the sky. By default, this method uses the real time capture option. If real time capture isn't necessary for your project, you can disable the real time capture from the Capt
ure Based Sky Light category. Note that Real Time Capture is not supported by all platforms, and is incompatible with Volumetric Fog.
2. Custom Cubemap: A simple static cubemap texture, set using the Custom Cubemap option below.
3. Cubemap with Dynamic Color Tinting: This method uses a flat grayscale cubemap and tints it dynamically with color to align well with the time of day. This is a good balanced option as its dynamic without requiring recapturing, and supports all platforms.Each Sky Light Mode has its own category of settings specific to the mode, found beneath the main Sky L
ight category.
-----
SIMULATING REAL SUN, MOON AND STARS USING DATE, TIME, AND COORDINATES
-----
In the Simulation category, you can enable settings which use a simplified astronomical simulation to map the position of the Sun, Moon and Stars.>• Simulate Real Sun will override the position of the sun, using a calculated position for the location, date and time provided.
• Simulate Real Moon will do the same for the Moon, and will also calculate the appropriate phase and orientation for the moon texture for the given time and location.
• Simulate Real Stars will replace the default tiling star texture with an accurate 360 degree starmap, pitched and angled correctly for the location and time. Note that the star map texture used for this is very high resolution, at 8192 x 8192. Consider that before using it on platforms which will downscale textures to a maximum size.
• Latitude and Longitude are how you'll input the desired location to be simulated. Make sure you also adjust the Time Zone, so that the Time of Day will be interpreted as expected for that location. The Time Zone is entered as a UTC offset. For example, the UTC offset for Eastern Standard Time is -5.
• Year, Month and Day control the date of the simulation. The day will automatically increment forward at midnight. Leap Years are taken into account. Also, these variables are replicated, so the current date will be shared by all clients if using networking.
• North Yaw can be adjusted to rotate the simulated compass directions clockwise. By default, +X is the direction of North.
• Simulation Speed controls how fast Time of Day is animated, if both Animate Time of Day and Simulate Real Sun are enabled. By default, the speed is set to 1, which is roughly a realistic speed.
• True Real Time can be enabled if you want your simulation to always reflect the actual current date and time at the simulated location. It does this by ignoring the Time of Day variable and instead timing the simulation using the system's reported UTC time. Note that because this accesses the current UTC time directly, it disregards the Time Zone setting.
• Apply Daylight Savings Time will change how the Time of Day is interpreted by the simulation. It will also make Time of Day change by 1 hour when the changeover happens twice a year. Because of this, if any Simulation option is enabled, all other Time of Day relevant systems will adapt to DST as well, to keep the system in sync with itself. You can adjust 
the time ranges of Daylight Savings Time from the advanced dropdown of the Simulation category.
• Date Controls UDW Season will adjust the Season variable on Ultra Dynamic Weather, if you have one in your map. It will do this using the current date, and the season will change with the time of year.Notes on the Accuracy of these Astronomical Calculations:>Because blueprint math isn't capable of the floating point precision necessary to do the complete v
ersions of the appropritate astronomical algorithms, what I've created here is my own approximation. It leaves out complicating nuances such as the eccentricity of the earth's orbit, or the irregularity of the earth's shape, in favor of making the calculation more managable for blueprint math. That said, I've done a lot of back and forth testing, and my appr
oximations of the sun's position were never more than a little over a degree off from the results given by the complete algorithm, and that deviation is a worst case scenario. Typically the deviation was only in fractions of a degree. Again, based on my own tests. You may find edge cases where the deviation is worse. Still, I think the accuracy of the sun is
 sufficient for almost all practical applications.
The accuracy of the Moon's position is more variable than the sun's. The Moon's orbit is calibrated using it's position in 2017. So, any date within several decades of that should be generally accurate. At the very least, the moon should generally appear in the correct constellation and have the right phase.
The stars position should actually be pretty much completely accurate. This is because the north pole of the Earth and the celestial north pole are the same thing, making the calculations much simpler to have total accuracy.
-----
ANIMATING THE SKY WITH SEQUENCER
-----
Here are some tips for animating UDS using sequencer:>• To animate Time of Day directly, you should disable the "Animate Time of Day" setting on UDS, and keyframe the Time of Day variable. When animating with the Time of Day variable, it's okay to go past 2400. The system will understand this and proceed forward in time with a new day.
• To animate the cloud coverage, you can keyframe the Cloud Coverage variable on UDS, but only if you don't have an Ultra Dynamic Weather actor in your scene. If you do, you should keyframe the Cloud Coverage variable on UDW instead.
• To directly animate cloud movement, first set Cloud Speed to 0 (or set Cloud Speed Multiplier to 0 on UDW if you have a UDW actor in your scene). Disable "Randomize Cloud Formation on Run" as well. Then in sequencer, animate using the Cloud Phase variable. This will allow you to directly control cloud movement in a way that will play back the same way ever
y time.
• If you need to animate a variable on UDS which isn't exposed to sequencer by default, you'll need to expose it in the variable settings. To do this, open UDS in the blueprint editor, and find the variable in the variable list. With it selected, find the option in the details panel called "Expose to Cinematics". Check this, and the variable will be availabl
e in sequencer for keyframing.
• For tips about animating weather, see the section about sequencer in the Weather Basics chapter of the readme.
-----
OPTIMIZING FOR PERFORMANCE
-----
With everything enabled at the highest quality, UDS can be demanding for some hardware to run. Here are some suggestions if the performance cost is too high for your project.If Using Volumetric Clouds:>• Try adjusting the View Sample Count Scale and Shadow Sample Scale. Reducing these will lower the cost of the volumetric rendering, but can introduce noise a
nd artifacts.
• Only use one layer of volumetric clouds. The option to use 2 layers is disabled by default because it has a significant performance cost.If Using 2D Dynamic Clouds:>• Try enabling the option to use only one 2D cloud layer. This can reduce the cost of the sky shader.
• Try the Sky Mode called "2D Clouds using Color Curves (Legacy Mode)". This mode derives all of its colors from curves instead of the sky atmosphere simulation. The coloring is less realistic as a result, but the performance cost is reduced.Misc Performance Tips>• Turn off Aurora effects in the Aurora category. These are actually disabled by default, as the
y add a signifigant instruction count cost to the shader. If performance is a priority, consider disabling these.
• Reduce the "Material Quality Level" scalability setting. The sky shader will reduce some minor aspects of its visuals based on Material Quality Level, including forcing a single cloud layer when quality is set to low. The Volumetric Clouds change significantly with Material Quality Level as well, changing the resolution of 3D noise used as well as the numb
er of texture layers sampled for both 2D and 3D layers of the shader.
• All of the lights on UDS are movable by default, but static or stationary lighting is always going to be a more performance friendly option if it can fit your project. You can adjust the mobility of each light from the Component Selection and Mobility category.
• You can also set the Sky Mode to change on launch with the current Effects Quality set in the Game User Settings. For example, you could make it so that settings Medium and above use volumetric clouds, while Low will use static clouds. You can do this by enabling "Use Sky Mode Scalability Map" in Basic Controls, under the advanced dropdown, and adjusting t
he map.
-----
CONSIDERATIONS FOR MOBILE
-----
If building for mobile devices, take note of the Mobile category. This category does several things by default to adjust the sky for mobile platforms.>• "Volumetric Clouds Replacement" will replace volumetric clouds on mobile platforms with a different sky mode. By default the replacement is Static Clouds.
• "Real Time Capture Sky Light Replacement" will change the sky light mode to a replacement if the sky is using real time sky light capture (which isn't supported on mobile). By default, the replacement is the dynamic tinted sky light. Note that if Captured is selected for this option, it will use a static sky light capture, which requires recapturing.
• "Adjust for Mobile Renderer" will adjust a number of lighting and material settings to adjust for various features the mobile renderer doesn't support.
• "Mobile Platforms" allows you to customize the list of platform names which UDS will consider mobile and apply the mobile overrides to. The defaults are Android and IOS.
-----
USING STATIC/STATIONARY LIGHTING
-----
To make any of your lights static or stationary, you can change their moblity in the Component Selection and Mobility category.
Once lighting is built, you will still be able to make changes to the sky settings, but note that any settings which alter the lights or move them around (Like changing Time of Day) will break the lighting build and you'll have to build again. Also note that if your Sun light is set to be static/stationary, this disables the Animate Time of Day setting, as t
he sun can no longer be moved in game.
-----
CONTROLLING TIME OF DAY FROM ANOTHER ACTOR
-----
If you have your own system for time of day and need to control the sky externally, the process for that is very simple. Just have your actor change the Time of Day variable in Ultra_Dynamic_Sky and the sky will update to the change you make on its own. Just make sure Animate Time of Day is disabled on UDS so that the two aren't conflicting.
You can also set the Time of Day variable using different time structures, using the utility functions on UDS. "Set Time of Day Using Time Code" and "Set Date and Time" are ones to try.
-----
TRIGGERING EVENTS AT SUNRISE AND SUNSET
-----
There are Sunrise and Sunset event dispatchers. These could be useful for toggling lighting that you only want enabled at night, or controlling an ambient audio system.
To use them, you'll first need to get a reference to the UDS actor in your blueprints. A simple way to do that is to use "Get Actor of Class". Then using that reference, you can bind events in your blueprint by running "Bind to Sunrise" or "Bind to Sunset". Once they're bound, these events will be called by UDS at the appropriate time. You can adjust the spe
cific time that they trigger in the Animate Time of Day category.
-----
SAVING THE SKY AND WEATHER STATE FOR SAVE DATA
-----
If you need to save the current state of UDS, and UDW as well if using it, for saving in save data or just preserving the state across a level load, there are functions on UDS to do that.>"Create UDS and UDW State for Saving" will package the state of both UDS and UDW into a single struct, which you can save with your save data. It contains all the variables
 for the time and current weather state.
"Apply Saved UDS and UDW State" will take in one of those saved state structs and apply it to UDS and UDW. This is to be used when loading a save or upon entering a new level.
-----
SAVING AND APPLYING CONFIGURATIONS
-----
It may be useful to save a full configuration of all the settings on UDS. You can do this using the configuration manager. You can find the configuration manager in the Blueprints folder, and run it by right clicking and selecting Run Editor Utility Widget.
In the configuration manager, you can select your existing saved configurations to apply to your UDS actor. And you can create new configurations using the save button in the bottom right, when no configuration is selected.
You will be prompted to name your new configuration and select a place to save it. You can either save to your project files, which will put the new config into the Ultra Dynamic Sky folder in your project. Or you can save to the engine content folder, which will put the config file into an Ultra Dynamic Sky folder there. If the config is saved in the projec
t, it will be accessible only from this project. If the config is saved to the engine, it will be accessible by UDS in any project using that engine version.
-----
USING LEGACY COLORING
-----
If you've selected the Sky Mode "2D Clouds Using Color Curves", the sky draws its colors from curves in the Color Curves folder. These curves are selectable from the Legacy Color category. If you make changes to them, remember to press "Refresh Settings" at the top of UDS settings in order to see the changes.
***
PART 2
WEATHER BASICS
-----
Ultra Dynamic Weather can add rain, snow, sound, material effects and more to your scene. You can control the weather changes in several different ways from random variation to directly calling a weather change.
-----
SETTING UP WEATHER IN YOUR SCENE
-----
To set up weather in your scene, first make sure you have an Ultra_Dynamic_Sky actor in your scene. The weather system will not operate without one.
To add weather, simply drag an Ultra_Dynamic_Weather actor from the Blueprints folder into your scene. It will detect the Ultra Dynamic Sky on its own and hook everything up.
-----
CHANGING THE STARTING WEATHER
-----
On the Ultra_Dynamic_Weather actor, in the Basic Controls category, you'll find all the settings to change the weather state in your map.
Weather Type will allow you to select a preset from a list of basic types. Partly Cloudy, Rainy, Blizzard, ect. Select one of these and it will be applied to all the relevant settings.
Normally, the settings entered here will define what weather the system starts with on play.
-----
ADJUSTING THE RAIN AND SNOW PARTICLES
-----
In the Rain and Snow Particles category, you'll find all the relevant settings for adjusting how precipitation particles are spawned and how they behave.
This emitter spawns particles in an area around the player camera, either in editor or in game. There are settings for how big this spawning area is and how many particles should be spawned. There is also an option to disable the particles collision.
The collision used by the rain and snow particles is very simple. It detects collision which blocks a specific channel specified in the settings as "Rain / Snow Particle Collision Channel". By default this is Visibility, so simple collision surfaces which block visibility traces will block rain and snow.
-----
SETTING UP RANDOM WEATHER VARIATION
-----
Random Weather Variation works like this: Periodically, the system will choose a new random weather type and transition to it gradually. You can define everything about how it does this, from the timing of the transition and type changes to the probability of each weather type.
If you want to enable random weather variation, you'll first need to check the box for "Use Random Weather Variation". The setting beneath that, "Start with a Random Weather Type" will determine if the settings from Basic Controls are used when the game is started, or if the system will choose a random starting weather.
Season controls which of the probability maps the system will use to choose a new weather type. By default, the settings reflect a climate with snow common in the  winter and rain common in the summer.
Weather Type Change Interval controls the min and max of how long the system will hold on a given weather type before picking a new random one to transition to.
The Weather Type Probability maps contain all weather types and a corresponding probability value. This value is proportional to the rest of the values in the map. Meaning, if one type is set to 5 and the rest are set to 1, that type will be 5 times more likely to be picked.
Transition Length defines how much time is devoted to transitioning between each random type, as a fraction of the period of time before the next change. For example, if we're waiting 100 seconds until the next change and the Transition Length is 0.5, then we will spend the first 50 seconds of that time transitioning to the current type.
-----
MANUALLY CHANGING THE WEATHER STATE DURING THE GAME
-----
If you want to transition (either over time or instantly) the weather state to a new type of weather while the game is running, there are two functions to do that:>1. Change Weather Using Type - Running this function will force Ultra Dynamic Weather to start transitioning to the supplied Type, over the course of the time input. If you have Random Weather Var
iation enabled, then after maintaining it for the supplied time, it will then transition back to Random Weather Variation over the supplied time.
2. Change Weather Using Settings - This function works the same way, but instead of a Weather Type, you can supply all of the specific settings you want.
-----
CHANGING WEATHER WITH LOCATION
-----
For large maps, it may be necessary to change weather by region. You can do this by using a Weather Override Volume, found in the Weather Effects folder in Blueprints.
A weather override volume can either apply a single weather type within its space, or it can generate its own stream of random weather variation, using its own set of probability maps. You can set which mode is used in Basic Controls on the weather override volume.
To adjust the area affected by the volume, edit the points of the spline component. You can right click on a point on the spline to add new spline points. You can also scale the actor, but try to avoid non-uniform scaling.
The variable "Transition Width" controls how much space is devoted to transitioning from the outside weather state to the inside weather state. The transition is completely spatial, so ideally the transition width should be very high, to offer a smooth transition between states as the player crosses into the volume. The default transition width is small to k
eep the initial size of the actor reasonable as a starting point. An ideal transition width would typically be much larger.
You can adjust the Priority variable to control what happens when multiple volumes overlap.
The effects of the Weather Override Volumes are dependent on the position of the player, so they're only visible when the game is running.
By default, UDW will test against the weather override volumes using the current player pawn location. You can adjust this behavior from the advanced dropdown of UDW's Basic Controls. The Control Point Source Location is what determines this.
-----
SETTING UP AND CONTROLLING MATERIAL EFFECTS
-----
Ultra Dynamic Weather can control material effects which make your materials respond to changing weather.
To use the included material effect functions, add them to your material from the Materials/Weather folder or just search for "weather" in the material function library in the material editor. There are two included basic functions. "Wet Weather Effects" and "Snow Weather Effects". (Dynamic Landscape Weather Effects is intended specifically for use on ground
 surfaces, and is covered in it's own section)
Wet Weather Effects can make surfaces appear wet by transitioning to a wet roughness value, appearing in the low areas of a height input first before covering the material completely. By default, it will lerp roughness to a value of 0.05 and base color will be darkened by 30%. You can adjust the specifics of how this transition looks using the inputs on the 
function. If you want to vary wetness across the surface, use the Max Wetness input to do so.
Wet Weather Effects also contains two extra effects which are disabled by default, but can add a lot to specific types of surfaces. One is a Puddle effect. Good for terrains/ground meshes, this will modify the normals to flatten out fully wet areas and introduce a rippling texture which responds to the current amount of rain. The other extra effect is a Drip
ping effect. This is good for walls and vertical surfaces. It maps a dripping texture in world space to make it look like water is trickling down the surface during rain.
Snow Weather Effects operates similarly to Wet Weather Effects, but it uses a built in set of default snow textures instead of static values. These can be replaced with your own textures using the available inputs.
Both functions have tooltips for all their inputs which explain the particulars of how to use each one. I'd recommend reading through those for more advanced tips.
-----
SETTING UP DYNAMIC LANDSCAPE WEATHER EFFECTS
-----
Dynamic Landscape Weather Effects is a special material effect function which can add dynamic interactive snow coverage and puddles to a landscape (or general ground meshes), but it requires more specific setup than the other material effects. To set this up, follow these steps:>1. Add the material function into your landscape material. The function is calle
d "Dynamic Landscape Weather Effects", and can be found by searching the material palette. You should typically insert the function at the end of your landscape material graph, so that the weather effects will be applied on top of everything else. The main inputs from Base Color to World Displacement are what the function will modify with the effects, but no
ne are individually required for the function to work. Just supply whatever inputs your material makes use of. The rest of the inputs are for masking the effects in whatever way suits your material setup. I'd suggest reading their tooltips for more info on each.
2. Disable the effects you don't need. The material function has static switch parameters to enable/disable the Snow or Puddles and several small additional effects. From your landscape material instance, disable  the effects your project doesn't need, to save on material instructions and texture samples.
3. On UDW, enable the setting "Enable Dynamic Landscape Weather Effects" in the category of the same name.
4. Calibrate the "Displacement Input Minimum Level" and "Displacement Input Maximum Level" if you have supplied a World Displacement input for the material function. These levels should correspond to how far the displacement will move the vertices at their min and max height level. For example, if I had a normalized displacement map, subtracted 0.5 from it a
nd multiplied by 10, then multiplied it by the vertex normal and plugged that into World Displacement, the Min and Max of that range would be -5 and 5. Calibrating this input correctly will ensure that displacement is used to affect the snow and puddle coverage correctly.
5. Add interaction components to objects you want to affect snow and puddles. The component is called "DLWE Interaction". You can find it in the Blueprints/Weather Effects folder. It is a self contained blueprint component which keeps track of its movement and when appropritate will draw compressions into the snow and ripples into the puddles. When adding th
e component, make sure to place it in the center of mass of the part of the object which will contact the ground. For example, to make a character model leave trails in the snow with their feet, you would add two DLWE Interaction components, as children of the skeletal mesh. You would set their parent socket to be the left and right foot sockets, and move th
e components so they sit in each foot's center of mass. When adding components, make sure to adjust their Size variable. This determines how far away the component will affect the landscape and how big the brush used for its effects. The size should be roughly the same as the diameter of the object. So for the character's feet, that would be rougly the lengt
h of the foot. By default, the interaction component will produce movement sound effects and particles. You can disable any of these from the component settings.For the effects, a tesellated material is obviously ideal. However, the material function can be used on a material without tesellation. If you do this, I would recommend you not use the World Positi
on Offset output on the function, as this is designed to correct shadow errors in conjunction with tesellation.
The effects are designed primarily for landscapes, but you can use them on a static mesh as well. To tell UDW and the Interaction components what surfaces the components should respond to (other than landscapes) you'll need to add physical materials to an array on UDW called "Physical Materials which Enable DLWE Interactions on Non-Landscapes". Make sure you
r static meshes are using physmats in that array, and the DLWE Interaction components will respond to their collision as they do to landscapes. Also, make sure your static mesh is of the object type for "Landscape Object Type" set on UDW. By default this is World Static.
The render target will dynamically recenter itself as your player pawn moves through the level. If you want this recentering to be based on a different location, you can do that. In UDW's Basic Controls, in the advanced dropdown, change the Control Point Location Source. This also affects how weather is changed by weather override volumes. By default the pla
yer pawn location is used, and should be a good fit for most projects. But you can change this to use the player camera location, or to control it manually using a vector variable.
For spawning sounds and particles, the interaction components approximate some of the logic happening in the material function, to dynamically determine if a spot has puddles or snow. They don't have any way of knowing about how you're masking the effects though, so you might run into situations where there are sounds and particles happening where there isn'
t snow or a puddle. To avoid this, you can have specific physical materials set to block these effects. In the advanced dropdown of the Dynamic Landscape Weather Effects category, find the physical material arrays for rain and snow. Adding to these arrays will ensure sounds and particles are not triggered on these phys mats.
-----
USING WEATHER SOUND EFFECTS
-----
By default, Ultra Dynamic Weather has sound effects enabled for wind, rain and thunder. You can completely disable the sound effects using the checkbox at the top of the Sound Effects category, or you can adjust the volume of each sound there as well.The sound effects on UDW are affected by a simple system of sound occlusion by default, which periodically se
nds out traces from the camera location and adjusts sound volume and low pass filter frequency if the player is in an enclosed space. This behavior can be disabled or adjusted from the Sound Occlusion category.
From this category you can also change the sound occlusion to use the Control Point Location (player pawn location by default) if that makes more sense for your project. For example, a top down game where occlusion whould be player centric instead of camera centric.
-----
ADJUSTING THE LIGHTNING EFFECTS
-----
There are two types of lightning in Ultra Dynamic Weather. Lightning Flashes and Obscured Lightning. Lightning Flashes are the big lightning bolts which can cast light into the scene and have a directly associated loud crash of thunder. Obscured Lightning is the particle effect which looks like flashes of lightning hidden in the cloud layer.
In the Lightning category, you can adjust the interval between flashes of both lightning type. You can adjust the behavior of the light source for lightning flashes (if you want one at all) and you can enable lightning during snowy weather as well (which is disabled by default).
If you need to manually trigger a lightning flash, you can do this. Just run the function Flash Lightning. It has inputs so you can give it a custom location to spawn in. Note that this location is the position of the root of the lightning bolt, so it should be at cloud level.
-----
ADJUSTING VOLUMETRIC FOG PARTICLES
-----
Volumetric Fog Particles add an element of volumetric fog to the rain/snow particles during particularly heavy weather. This effect will only be visible if you have volumetric fog enabled on your height fog in UDS.
The "Max Fog Particle Percentage" variables control how many of the rain or snow particles will be accompanied by a fog particle. They are coupled together so that the fog particles can piggyback off of the collision calculations the rain and snow is already performing, allowing the fog particles to benefit from collision for no extra cost.
-----
CONTROLLING A WIND ACTOR
-----
You can make Ultra Dynamic Weather control a Wind Directional Source Actor using the current wind speed and direction. Just select one from the scene in the Wind Actor category. As weather changes, the speed of wind will be controlled. The amount of wind speed applied can be adjusted using a setting in that category as well.
-----
SAMPLING TEMPERATURE
-----
There is a function on UDW called "Get Current Temperature", which you can use to sample the current temperature in Fahrenheit and Celsius. This value is generated in a very simplified, approximated way, and is just meant to be used for gameplay purposes.
Here's how the temperature system works:
The system starts with a base temperature. This is determined by the current season, using the Base Temperature variables in the Temperature category.
This base value is then modified by the Factor variables in the Temperature category, using the current weather and time of day.
Then the resulting temperature is clamped inside the Valid Temperature Range.
The default values for all of these inputs are set with Fahrenheit in mind, but you can use Celsius values if you prefer. Just change the Temperature Scale at the top of the Temperature category, and supply all of the variables with your own appropriate Celsius values.
-----
USING WEATHER WITH SEQUENCER
-----
Here are some tips for how the weather system can be animated using sequencer.>• To animate the current weather state in a way that will play back the same every time, use the exposed variables (the same ones from Basic Controls) for Cloud Coverage, Weather Intensity, Wind Intensity, and Rain/Snow.
• To animate cloud movement in a way that will play back the same every time: First, set Cloud Speed Multiplier to 0 on UDW. Then, turn off Randomize Cloud Formation On Run, in Cloud Movement on UDS. Then in Sequencer, animate the Cloud Phase variable on UDS. This will allow directly controlling cloud movement with keyframes.
• When previewing a sequence that contains rain/snow, note that the particles will not be visible during the playback preview in editor. This is just a limitation of sequencer's preview. It's unfortunate, but as of now there is no workaround. To test how particles are looking at a specific place in the animation, pause the playback there and the particles sh
ould resume.
• Lightning flashes, being animated by blueprint logic, will not be visible when previewing sequences either, though they will be visible if rendering a sequence or running one in game. If you want direct control over the timing of lightning flashes in your animation, disable Spawn Lightning Flashes on UDW, and run the UDW function Flash Lightning using an e
vent track on your sequence. The Flash Lightning function also has inputs for providing a custom location for the lightning flash. With all of this together, you can animate lightning to flash at the specific time and place in the animation that you want.
• To directly animate material effects (Wetness and Snow Coverage), first disable "Simulate Changing Material Effects with Weather" and then animate using Material Wetness and Material Snow Coverage.
***
PART 3
TECHNICAL DOCUMENTATION
-----
This document of technical notes will run through the major points of how Ultra Dynamic Sky's blueprint and materials work together. It's intended for users who want to do their own modifications to expand UDS's capabilities to suit their particular project. It assumes a working knowledge of blueprint and material workflows in UE4.
-----
SYSTEM OVERVIEW
-----
To start these technical docs, here's a very broad breakdown of the two major blueprint classes included and what each handles.^Ultra Dynamic SkyUDS contains all of the components and logic for rendering the sky, the clouds, and controlling the time of day. Here's a general list of what UDS handles:>• Contains all of the visible components of the sky. The sk
y sphere, volumetric cloud and aurora components, the sky atmosphere component, directional lights for the sun and moon, and exponential height fog.
• Creates dynamic material instances for the sky, clouds and cloud shadows. The settings of these dynamic instances are controlled using the current UDS settings, based on cloud coverage and time of day.
• When the game is running, depending on the settings, UDS can advance Time of Day forward at a speed customizable in the settings. It can also periodically udpate a captured sky light, and increment the moon's phase.
• If movable, UDS will rotate the directional lights based on Time of Day.
• Settings on height fog, the sky light, and directional lights will be adjusted based on time of day and cloud coverage.^Ultra Dynamic WeatherUDW contains all of the logic for controlling weather effects and dynamic weather changes. >• Contains the niagara systems for rain, snow and obscured lightning flashes. Also contains all of the audio components for w
eather sounds.
• Contains the logic for weather changes, using both "Static" settings, meaning settings specified using specific values from the Change Weather functions, and "Random" changes, which are modified by the Random Weather Variation system. The system is designed to allow transitioning smoothly back and forth between static and random settings.
• Contains the logic for spawning lightning flashes, if enabled.
• As current weather settings are changed, material effects in a shared material parameter collection can be changed dynamically as appropriate.
• Contains logic for controlling Dynamic Landscape Weather Effects, managing the render targets and recieivng intereactions from DLWE Interaction components.
• Contains the logic for adjusting audio levels and parameters based on current weather, and occluding sound volume based on the position of the camera.These two blueprint actors, when placed into a level together, will detect each other using their construction script and can control each other's variables in some cases. UDW will take control of Cloud Cover
age and Cloud Speed when its present.
-----
MATERIALS
-----
This documentation won't cover how every detail of an entire material works, but I will try to summarize how all of the pieces fit together, so you can at least know where to look if you want to change or add something.1. Ultra_Dynamic_Sky_Mat
2. 2D_Cloud_Shadows
3. Volumetric_Clouds
4. Volumetric_Cloud_Shadows
5. Static_Clouds
6. Inside_Clouds_Fog_Particle
7. Volumetric_Aurora^Ultra_Dynamic_Sky_Mat>The structure of this material might be a little intimidating, but it should start to make more sense if you see where the path starts.
Basically, the material begins by drawing the "Base Sky Color", in that function. Legacy Coloring determines base sky coloring using some gradients from the Moon and Sun Gradients sections, whereas Sky Atmosphere coloring just uses SkyAtmosphereViewLuminance, plus Night Sky Glow.
Once base sky color is figured out,  the Cloud Wisps are added on top using Ambient Color. The wispy background clouds are the static texture of stratocirrus clouds that appear behind the dynamic clouds.
After that, the sun disk is added in. The disc is drawn by comparing the sun vector "Sun Position" to the camera vector, and filtering the difference. That's then multiplied over the sun's color, which is a parameter in Legacy Coloring, and based on LightIlluminance in Sky Atmosphere.
Then, the cloud layers are lerped on top, in the "Add Dynamic Clouds" section.
The Composite Cloud Layers function contains the two "Cloud Layer" function nodes, one for each layer.
The Cloud Layer function is a pretty big beast, and this doc isn't going to get into how it all works exactly. Basically, several moving cloud textures are mapped in the Map Cloud Textures function, then filtered in a variety of ways to produce several outputs in the Output Alphas section.
• A mask alpha of the clouds, which is used to mask out the stars/auroras.
• Soft shadow alpha, which is only used for the shadowing of shine effects present when using two cloud layers.
• A blend alpha. which is used to blend the cloud color into the rest of the shader.
• And color, which is the actual RGB output which is lerped to in the main material.
The cloud layers section draws some more info from the Shading Gradients function. This section is just what it sounds like. It creates a set of 0 to 1 gradients, centered around the sun and moon. Some of this is only used for legacy coloring.
There's also a function called Cloud Distribution. This applies the density multipliers selected in the Cloud Distribution section of the UDS settings. It multiplies them over cloud density and sends them into the cloud layer functions.
Back in the master material, after the cloud layers are blended in, there's a section called "Scales intensity around the sun". This just uses a few gradients to make the sky more intense in the area around the sun (and the moon).
The next thing in the main material is the Moon, Stars and Auroras. Because these are all additive effects, they just get added together (and masked by the clouds) before being added on top of the main line.
The stars are pretty simple. It's just a single tiling texture (the green channel of wisps+stars+moonsprites) panning with stars speed, and multiplied over Stars Color and Stars Intensity. It's also multiplied over the reverse alpha of the moon before being added in, so the stars appear blocked by the moon.
The moon is mostly handled inside the Moon material function. That material function handles outputting both the gradient for the moon's glow, and the texture itself, both mapped using the Moon Light Vector.
The 2d auroras are also handled in their own function. That function basically works by overlaying a several texture samples (the amount of which is dependent on material quality) in order to produce the distinct anisotropic radial blur of the aurora.
Once the additive effects are added into the main line, the only things left is scaling with the "Overall Intensity" value, controlling the saturation using the master saturation control and boosting contrast using the constrast setting.
The main material graph is also where the logic is kept for the customized UV sets which drive the clouds, in the section Cloud UVs. UV channels 0 through 4 are handled like this in the vertex shader to reduce pixel shader instructions.^2D_Cloud_Shadows>The cloud shadows material is not too complicated. It uses four texture samples to approximate the same tw
o cloud layers the main sky material is showing. It does this using the same variables for Cloud Density, softness, speed, ect. And it filters the clouds using the same Filter_Clouds material function. Then it just uses Shadows Intensity to determine how dark the light function goes.^Volumetric_Clouds>The volumetric clouds material essentially has two parts.
 One part on the left is outputting into the Volumetric Advanced Output. This controls the "conservative density", basically the 2D outline of the major cloud formations. And some global settings for cloud shading and multiscattering.
The part to the right of that outputs into a normal material output. This controls the per-sample extinction value returned by the shader as the volumetric rendering raymarches through the cloud layer.
All of this is determined by two types of textures. One is the "Clouds Basetex". These are 2D cloud textures, the same ones used by the 2D dynamic clouds. These are used to generate the conservative density, as well as add some large scale variation to a few other spots in the extinction value network.
The other texture is a 3D clouds texture used for the erosion and high frequency noise. This is what turns the clouds from 2D extrusions into realistic 3D shapes. On High and Epic material quality, there are 2 octaves of this 3D texture in use. On Low and Medium there is only 1.
Several places in the material, you'll see the Cloud Sample Attributes node in use. This allows the material to determine things based on how high in the cloud layer the sample point is.^Volumetric_Cloud_Shadows>The logic here is the same basic thing as the 2D cloud shadows, but it contains extra logic to allow it to accurately represent the real 3D size and
 shape of the volumetric clouds. It also tests the function against Z location along with clouds altitude so that shadows are cast at the appropriate angle and don't appear above the cloud layer.^Static_Clouds>This is the material used to render the clouds for the "Static Clouds" sky mode. It uses a set of textures combined with the current lighting angles t
o produce an approximation of lit clouds.
The section Create Cloud Shading is what samples the textures and the lighting angles, and creates a shading mask out of them. Basically, the input textures include lighting from 4 directions + up, and these are blended using either sun direction, if it's day, or moon direction if its night.
The rest of the material blends the light and dark cloud colors together (using the same function as the sky shader's 2D clouds) and then matches all of the sky shaders extra modifications, for things like saturation and contrast control.
There's also a bit which multiplied the opacity of the clouds using cloud density, so the static clouds fade away when the sky is overcast. This transition isn't the best looking in practice, but it allows static clouds to support weather.^Inside_Clouds_Fog_Particle>This material is used by a niagara system on UDS. It increases fog density inside clouds, whe
n using volumetric fog.
The material itself just replicates the exact same logic as the volumetric cloud shader, using the same functions. It then also multiplies that by another 3D volume texture sample, to add another small scale layer of turbulence to the local fog.^Volumetric_Aurora>The material setup for the volumetric aurora is much simpler than that of the volumetric clouds.
The conservative density uses 3 2D texture samples to define the shape of the whole aurora field. Two of them are compared with a distance node to create the distinctive aurora pattern, and the third is a larger sample, multipled over that in order to vary aurora intensity across the sky.
The extinction value mostly just takes the conservative density and applies a falloff using the normalized altitude, so the aurora looks strong at the bottom and fades at the top. A second layer of the conservative density is used to combine the aurora colors, which is used for the emissive output.
-----
ULTRA DYNAMIC SKY BLUEPRINT
-----
1. Components
2. Construction Script
3. Set Sun and Moon Root Rotation
4. Update Active Variables
5. Update Static Variables
6. Event Graph^Components>• Ultra_Dynamic_Sky_Sphere: The sphere mesh for the sky. Construction script assigns this the dynamic material instance for the sky material.
• Sun_Root: This is an arrow component which acts as a placeholder for the sun's rotation, irrespective of what the actual sun light component is.
• Moon_Root: The same, but for the moon.
• SkyAtmosphere: The sky atmosphere component controls coloring of the sky and lighting when enabled.
• Sun: The built in directional light component for the sun.
• Moon: The same for the moon.
• HeightFog: The built in exponential height fog component.
• Exposure: A post process component which applies a min and max for auto-exposure.
• Capture Based Sky Light: The built in sky light component for when a capture based mode is selected.
• CubeMap Sky Light: The built in sky light component for when a custom cube map or cube map with dynamic color tinting is selected.
• VolumetricCloud: The component which renders the volumetric clouds when using that Sky Mode.
• StaticCloudsSphere: The mesh for rendering the static clouds in that sky mode.
• VolumetricAurora: The component used for rendering volumetric auroras, when that sky mode is selected.
• Inside_Cloud_Fog: A niagara particle system which renders a volumetric fog particle on the camera's position whenever the camera is inside the volumetric cloud layer. This allows the volumetric fog to increase when inside a cloud.
• Box+CloudsFogPostProcess: A post process volume which allows clouds to fog the screen when the camera goes inside them, with the box to provide the bounds for the effect so it's only applied when it needs to be.^Construction Script>The construction script handles everything that needs updating when the user changes any of the exposed variables. It does the
 following, in order:>• Sets Refresh Settings to false. The refresh settings just acts as a way for the user to force constuction script to run without adjusting any settings, if necessary.
• Creates the Cloud Shadows dynamic material instance and saves it to a variable, Cloud Shadows MID.
• Clamps the Dawn Time so that it can't be set to later than the Dusk Time.
• Enables or disables the sky atmosphere component, based on if the user has selected the feature or not.
• Enables or disables the Volumetric Clouds, based on the sky mode, and enables/disables the niagara system for inside cloud fog if selected/applicable.
• Controls Cloudiness on the Weather bp if necessary and clamps other values controlled by weather.
• Sets the Sun and Moon components based on what the user has selected in the Component Selection and Mobility section. The component will be set to the internal one, set to the external actor's light component, or disabled, depending on the settings. It also sets mobility of the resultant component.
• Sets the sky light component. Similar to the sections for setting the sun and moon components, but based also on "Sky Light Mode', a setting which determines the source type for the sky light.
• Sets the fog component. Functionally the same as the moon and sun part, but without mobility.
• Creates the Sky dynamic material instance, on the Ultra Dynamic Sky Sphere, and saves it as a variable, Sky MID. The instance it is based on it determined by several boolean variables representing the different features enabled.
• Creates the material instance for the volumetric clouds material.
• All update functions are run to update lighting and material settings based on current variables.
• Exposure settings are enabled or disabled, and the exposure range is set in the post process settings.
• The sky light is recaptured if it uses a capture based Sky Light Mode. If it doesn't, the cube map is set based on which of the other two sky light modes is in use.^Set Sun and Moon Root Rotation>This function sets the rotation of the sun root component and moon root component, based on Time of Day, as well as variables relevant to the path of the sun and 
moon, such as Sun Inclination and Moon Orbit Offset.
The first thing it does is create an Internal Time of Day, basically remapping Time of Day with Dawn and Dusk Time, so that Internal Time of Day has a Dawn and Dusk at 0600 and 1800. Which is necessary for the rest of the function to operate correctly.
The rest of the function is just the math for determining rotation on the sun and moon. This function just sets the root rotations. The "Update Directional Lights" function is then used to apply those rotations to the actual lights.
If Simulate options are enabled, this function runs the "Approximate Real Sun Moon and Stars" function to determine the angles.^Update Active Variables>This function sets any parameters and component settings which can change dynamically during the game, either with changing time or weather.
The vast majority of the first part should be self explanatory, as it's mostly just setting material parameters, with at most some simple math to turn the variable into the parameter.
After the first line finishes, there's a branch node where the function checks "Automatically Set Advanced Settings Using Time of Day".
If that's true, it continues to the full setup for controlling all of the time of day dependent settings, with a different section for each component.
If it's false, it sets the "advanced settings" using the advanced variables. The "advanced settings" is really only compatible with legacy color, as most of those settings only get used by that version of the material.^Update Static Variables>Functionally the same thing as the above function, but this one controls parameters and settings which are set once a
nd then remain static while the game is running.^Event Graph>The Event Graph is where the sky is initialized on event begin play and on Event Tick the sky updates any variables or components which need updating as the game is running. It handles the following:>• Day / Night Cycle: Increments Time of Day, taking into account variables like Day and Night Lengt
h, and Dawn and Dusk Time.
• Sunset / Sunrise Events: Fires event dispatchers for sunrise and sunset, at a specific time specified by the user in "Sunset Event Time" and Sunrise Event Time".
• Lunar Phase Changes: Increments the phase of the moon forward once per day.
• Periodic Sky Light Recapture: If the sky light is capture based, this forces a recapture, at a frequency set by the user.
• Refreshing the Sky: This just runs the Set Sun and Moon Rotation and Update Active Variables functions after all of the above, to refresh the lighting and sky material with the new values.
By default, most of these tick operations are affected by an optimization which distributes them across 3 frames, using the macro called "Tick Set Gate".
-----
ULTRA DYNAMIC WEATHER BLUEPRINT
-----
1. Components
2. Construction Script
3. Event Graph
4. Event Tick
5. Update Active Variables
6. Update Static Variables
7. Update Audio
8. Increment Random Weather
9. Set Material EffectsComponents>• Rain and Snow - This is the niagara system which spawns rain and snow particles.
• Lightning Light - This is the directional light which accompanies lightning flashes when the feature is enabled.
• Obscured Lightning - This is the niagara emitter for the obscured flashes of lightning.
• Audio components - The rest of the components are for the ambient audio sources. These are used only if Sound Effects are enabled.
• Post Process Wind Fog - A post component which applies a simplified volumetric effect to heavy weather, if enabled.
• The Random Weather Variation blueprint component. This handles creating the stream of random weather variation. It's handled as its own component so that the Weather Override Volume class can use the same logic.^Construction Script>First, the weather BP finds a reference to the UDS actor, so that it can control cloudiness, cloud speed, and cloud direction.
Then, once it makes sure it has a reference, it applies a weather preset if one has been selected from the dropdown.
Then, it just runs all of the update functions, including running the construction script on the UDS actor to have it update with any changed settings as well.^Event Graph>In the "Create Real Niagara Systems" section, the niagara components are disabled and replaced with newly spawned components. This is to workaround a crash which can sometimes occur on nia
gara systems that rely on camera data.
In the "Initialize Random Weather Variation" section, the RWV component is started if the feature is enabled, and its first weather setting is used to set the starting weather state.
In the "Initial Setup" section, starting variables are created and components activated to begin things like the sound occlusion system and the post process wind fog.
The Event Graph is also where the Change Weather Using Settings and Change Weather Using Type functions are located as custom events. Both of these start by setting the new versions of the target variables, then starting the transition by setting the Transition State integer and setting the old versions of the weather variables.^Event Tick>Event Tick starts 
by running the logic that increments a transition, either from a static weather state to another static weather state, or into/out of random weather varitation. Then, whatever the outcome of that, it runs Update Active Variables to set the current weather variables and update everything.
The next section periodically flashes lightning on the global weather state, the interval determined by Lightning Flash Interval Random Range.
Update Dynamic Landscape Weather Effects handles all the periodic updates and recentering needed for the DLWE effects, if they're enabled.^Update Active Variables>Update Active Variables, similar to the function of the same name on UDS, updates variables, parameters and settings which can change during gameplay.
It starts by updating the "Current" weather variables, the ones which represent the visible state of the weather and sky. It does this by lerping between the static values and the current random values, based on the state of the transition system.
It then sends the updated relevant variables to the UDS actor.
The next section updates all of the active parameters on the rain and snow niagara emitter. Things like spawn rate , wind strength. Anything that changes with weather.
The Obscured Lightning gets its spawn rate based on current weather.
Then the system updates the speed on the Wind Actor if one is selected.^Update Static Variables>Same as on UDS, this function sets parameters and settings which are set once and then never updated during gameplay.^Update Audio>This function updates all of the volumes and audio parameters for the sound effects.
The dynamic wind sounds is the more complicated part of this. There are 4 main wind audio components, in the four cardinal directions. Each gets its low pass, pitch, volume set by the current weather state. And the volume is modulated by the direction of the wind as well, so that the wind sounds slightly louder from the direction the wind is coming from.
The rain and thunder sounds are simpler. The rain sound cue contains the logic for fading between the different rain sounds based on weather intensity. This section just sets that Intensity float parameter and overall volume based on a float curve..
-----
NIAGARA SYSTEMS
-----
1. Rain_And_Snow
2. Obscured_Lightning
3. Lightning_Strike
4. Inside_Cloud_Fog
5. Dripping_Curve^Rain_and_SnowThis niagara system handles spawning for both rain particles and snow particles together, as well as the volumetric fog particles if enabled. It uses a large set of user parameters to change its behavior based on the current weather. Here's what every module of the rain and snow emitter is doing, generally.
On Emitter Update:>• In the module "Get Camera Variables" A Camera query is used to get the current camera position, and that value is compared against the last frame's camera position to extract the camera's current velocity as well. These are emitter level attriibutes.
• In the module "Determine Spawn Origin", the camera data and a number of user parameters are used to find the center point for the volume which will spawn particles for this frame.On Particle Spawn:>• The "Freeze" module decides if this particle should be snow or rain, depending on the current user parameters fed to the system by UDW.
• "Determine Specific Velocity" takes in  a General Velocity from UDW which represents the average velocity of the current rain/snow particle field. It then mutates this general velocity with randomness and varies the velocity based on if this particle is snow or rain. The resulting "Specific Velocity" vector represents the exact velocity this particle will 
travel at for its whole lifetime.
• The particle is initialized with its lifetime and size.
• Cylinder Location is what determines the location of the particle, using the Spawn Origin created in Emitter Update + the distribution and height variables.
• Check Collision Along Path is what handles the collision query for the particle. It's a CPU collision query against simple collision, so for performance, only one is used to handle all of the necessary behavior. The trace starts from a point set back from the particle's location, along specific velocity, and ends down its path along specific velocity. If t
he collision query hits something between the start and the particle position, it kills this particle immediately without it ever displaying. (This is because if a collision was detected in that range, the particle is probably trying to spawn indoors). If a collision is detected in the rest of the range, that point is used to determine the Death Height, and 
the normal of the collided surface is saved and used to determine if a splash effect should be spawned.
• Color is determined.
• The specific velocity is applied to the particle's physics velocity.
• A random SubUV frame is selected. Both rain and snow use a 2x2 subUV sheet, so this behavior is the same for both.
• Some attributes are determined for refraction and particle doubling. Refraction is an effect which exists for both rain and snow, but is most noticable on rain particles. The amount of refraction determines how much rain particles distort their scene color sample for the refraction effect. Particle Doubling is something the rain snow particles do when weat
her intensity is very high. Basically, there's a second Sprite Renderer, which will render the rain or snow particle twice, if this particle is doubled. The double is offset backwards along the Specific Velocity, so it follows the real particle. This helps to increase the apparent density of the particle field for no extra particle calculation cost, and its 
only applied at levels of weather intensity where you can't really see the doubling.
• Dynamic material parameters for the rain/snow material are calculated. Param 1 just represents if the particle is rain or snow. Param 2 Is the X refraction multiplier for the particle. Param 3 is the Y refraction multiplier. Param 4 is the overall refraction amount for the particle, different for rain and snow.
• Some attributes are calculated for volumetric fog particles. The size and camera offset of the fog, as well as the dynamic material parameters. Through the dynamic parameters, the fog takes in information about the particle's collision point so it can mask itself in 3D space to not appear at all on the opposite side of the collision surface.On Particle Upd
ate:>• "Detect if Particle Has Reached Death Height" is what determines if the particle has hit something, based on the collision data collected on particle spawn. If the particle's position is lower than the death height, the particle is killed (Alive is set to false) and Hit Ground is set to true. Though, if the particle is snow and "Snow Sticks to Surface
s" is enabled, then the particle doesn't die at this point.
• Solve Forces and Velocity applies a max speed.
•  Scale Sprite Size By Speed is what makes the particles stretch out based on their speed, for an approximation of motion blur. Rain is affected by this more than snow.
• Generate Death Event is what sends the event which spawns a splash particle, in the Splash emitter to the right.
• The particle's distance from the camera is calculated.
• The alpha of the material is scaled using a curve, so that particles fade in and out at the beginning and end of their lifetimes.
• The Twirl Offset is calculated for snow particles. This is an offset to the rendered position of the main snow particle, which causes it to have a fake "twirling" motion down through the air. Fake in the sense that it doesn't represent the actual position of the particle, which is always moving in a perfectly straight line to abide by the collision system.
• The position of the particle double and the main particle is calculated, to be used on the sprite renderers.
• Current fog color, visibility, and render position is calculated.
• The current rendered scale of the main and double particles are calculated.The Splashes Emitter:>The emitter for the splashes is much simpler. It just spawns one particle when it recieves the death event from the rain and snow emitter. It also has two sprite renderers, one for looking at the splashes from sideways, and one for looking at them from above. T
hey use the same material, but with different material parameters to render differently in the shader.^Obscured_Lightning>This system spawns the passive lightning flashes which are supposed to look obscured within the cloud layer, with no visible bolt.
Like the rain and snow system, it gets camera position to use as a center for the spawning area, and its spawn rate is set by UDW using a user parameter.
The intensity of the flash is animated using an "Animate Intensity" module in particle update, which combines a base curve and a random sample of a noisy curve to create a good flickering in and out animation.
The resultant intensity is delivered to the material in the Color, through the alpha channel.
Determine Facing and Alignment Angles is what determines if the bilboard faces the camera (if the lightning is far) or faces straight down without pivoting (if the lightning is near).
The size of the sprite is also scaled by distance from the camera, so that distant flashes are more stretched horizontally, to give the impression of foreshortening.^Lightning_Strike>This system spawns a single lightning bolt, with all the accompanying sprites and fake lighting.
Lightning Flare spawns the exact same material as Obscured Lightning, using the same animation setup. It just spawns only one.
Lightning Ball and Lightning Bits are very simple derivatives of the Lightning Flare which just add extra layers to the effect. Ball is a light flare just at the root of the lightning bolt, which flashes quickly. Bits are extra flashes which happen at random times near by the root location.
Lightning Bolt is the emitter which draws the main bright line of lightning. It does this using a ribbon renderer. Basically, Lightning Bolt has a very high spawn rate, and every time it spawns in a particle, it incremements an emitter attribute called Current Particle Position using an offset called Current Offset, and it mutates the Offset randomly as well
. This leads to a particle trail that snakes downward tracing a jagged line. The individual particles animate intensity the same way the Flare does, so they path of the lightning kind of flickers and buzzes as it fades out.^Inside_Cloud_Fog>This system spawns a single volumetric fog particle which renders at camera location if the camera is within the volume
tric cloud layer.
The emitter is very simple. On Emitter Update, it gets Camera Position using a camera query. In Particle Update it checks if that camera position is inside the cloud layer, and sets visibility of the particle accordingly.
The sprite renderer uses a dynamic material instance created by UDW, which has the clouds altitude and settings set from the UDS update functions.^Dripping_Curve>This is the system contained in the Rain Drip Spline BP. It spawns the same rain particles as the Rain and Snow system, and spawns splashes using the same event structure. The main difference is how
 it gets the data from the controlling BP, for the spline and the collision.
The start of the process is two user parameters, Death Heights and Positions Along Curve. These are arrays. Floats for Death Heights and vectors for Positions Along Curve. The Rain Drip Spline BP generates these arrays in a function called Create Curve Data. The Positions Along Curve is a series of locations along the spline component, evenly spaced. Death H
eights is the Z position of a collision resulting from a line trace aimed straight down from each of the positions along curve.
The emitter behavior is much the same as the rain and snow, just with some elements cut out for snow and fog behavior. The spawn location is derived from the Positions Along Curve array, and the individual Death Height for each particle is derived from the Death Heights array as well.
***
PART 4
***
-----
THE SKY COLOR FLICKERS BLACK WHEN MOVING THE CAMERA
-----
If you notice the color of the sky flickering to pitch black when the camera is moved in certain places in your level, you're probably encountering an engine bug with the sky atmosphere system.
The issue is caused in some circumstances by the camera going below the "ground" defined by the sky atmosphere component.
So the best solution is to select the Sky Atmosphere component in UDS (found in the component list at the top of the details panel) and move it down to the lowest point in your level, below where the camera can go.
-----
LIGHTING ARTIFACTS IN CLOUDY WEATHER USING RAYTRACING
-----
The raytraced reflections and global illumination cannot factor in the light function used to occlude the sun and moon during cloudy weather. As a result, with default settings, cloudy weather produces artifacts in reflections and indrect light.
There's a setting which can fix this on UDS. In Basic Controls, turn on "Dim Directional Lights with Cloud Coverage". This turns the actual intensity of the sun and moon down to 0 as clouds form, so that ray traced effects can work generally as expected.
-----
BROKEN WEATHER PARTICLES WITH RAYTRACING
-----
If you have Raytraced Translucency enabled, weather particles like rain, snow and lightning will be broken.
This is just a result of Raytraced Translucency being incompatible with translucent sprite bilboard based particles. The only fix is to disable Raytraced Translucency. You can do this on a post process volume. In the Tranlucency section, change Type to Raster.
-----
AMBIENT LIGHT NOT UPDATING AS TIME OF DAY CHANGES
-----
If you notice that the ambient light starts out looking correct, but as time of day changes, the ambient light doesn't update, it's almost certainly a problem with the sky light not updating. Here are a few possible causes of that:>If you're using the Sky Mode called "2D Clouds Using Color Curves" then this would happen because the Sky Light cannot use real 
time capture without the sky atmosphere. You'll need to change to a different sky light mode when using that sky mode. I would suggest Cubemap with Dynamic Color Tinting.
If you see this problem on specific platforms, it's probably because they don't support real time sky light capture. Again, I'd recommend changing Sky Light Mode to Cubemap with Dynamic Color Tinting for a good dynamic option that works on any platform.
If you specifically notice ambient light remaining bright as night falls, you could also just have static light from an old lighting solution present in your map. To check for that, just run a lighting build, from the Build dropdown on the main editor toolbar.
-----
RAIN/SNOW PARTICLES NOT SHOWING IN SIMULATE MODE
-----
If running in editor using the "Simulate" play mode, rain and snow particles will probably not be visible.
This is just a limitation of Simulate mode and the niagara interface the particles use to access camera data. In Simulate, the particles can't get the camera location, so they only spawn around the origin.
Since this is an engine limitation, there's no workaround at this time.
-----
SNOW COVERAGE AND WETNESS IN INTERIORS
-----
After adding snow and wetness material effects to your materials, you might be disappointed to find that without additional work they show up in interiors.
This is normal. The material functions pixel and vertex shader logic have no way of knowing what context they're used in. They don't know if the surface is "inside" or not. And the best way for a material to sample that information will vary from project to project and from material to material.
Whatever method you want to use, there are inputs on the functions to mask the effects. "Max Snow Coverage" on Snow Weather Effects, and "Max Wetness" on Wet Weather Effects. These take in a 0 to 1 mask which completely blocks formation of snow or water at a value of 0, and covers the entire material in either at a value of 1.
A simple and cheap method of controlling this mask in a static way is to use a vertex color channel. You could plug a channel of vertex color into Max Snow Coverage and paint the mesh in the level editor to define what parts form snow, for example.
-----
DLWE INTERACTIONS NOT HAPPENING WHEN THEY SHOULD
-----
If you've set up DLWE (following the directions laid out in the DLWE section of this readme) and interactions aren't happening, here's a list of things to check:>• Make sure your landscape (or static mesh) has simple collision using the Object Type specified by "Landscape Object Type" in the DLWE settings on UDW. By default, this is World Static.
• Make certain "Enable Dynamic Landscape Weather Effects" is on.
• Make sure the DLWE Interaction component is positioned and has a size big enough to trigger interactions with the surface.
• If you've modified "Render Target Resolution" in DLWE settings, make sure you've actually changed the resolution of both the render targets in Textures/Weather to match.
-----
BRIGHT AMBIENT LIGHT IN INTERIORS
-----
If using UDS with its default setup with all movable lights, you'll notice that interior spaces recieve as much ambient sky light as exteriors.
This is because a movable sky light in UE4 isn't a shadowed light source. To have your sky light shadow interiors, you have a few options:>• The best option in many cases, providing your project can support it, is to use a static or stationary sky light. Doing this will allow realistic soft sky light shadowing to be baked into your level's lightmaps when you
 run a lighting build. You can change the mobility of the sky light from the Component Selection and Mobility category.
• For a dynamic solution, you might try using Distance Field Ambient Occlusion. To enable this, make sure you've turned on the project setting "Generate Mesh Distance Fields" and the setting "SkyLight Casts Shadows" is enabled in the Sky Light category on UDS. DFAO is a realtime occlusion of the sky light contribution. If the meshes in your scene have good d
istance fields, this can offer decent occlusion of small interior spaces. But as a realtime solution based on the simplified geometry of distance fields, it will necessrily have some artifacts.
• Lastly, there's ray tracing for more of a brute force approach. Ray traced ambient occlusion and ray traced global illumination can greatly improve the realism of fully dynamic lighting in interiors. But obviously the hardware requirements are steep.
-----
VOLUMETRIC CLOUDS DON'T RENDER IN FRONT OF OBJECTS
-----
If using the default settings, you might notice clouds appearing incorrectly behind scenery that they should block.
By default, the volumetric clouds in UDS are optimized for typical use cases where the clouds exist entirely as a background layer. This allows them to prioritize fidelity and temporal stability.
If you need your clouds to render over the landscape/objects in your scene, the fix is simple. In the Volumetric Clouds category on UDS, just change the "Volumetric Cloud Rendering Mode" to one of the settings called "Clouds Render Over Opaque Objects".
-----
RAIN AND SNOW PARTICLES NOT COLLIDING WITH OBJECTS
-----
If you're having trouble with rain or snow particles not being blocked by objects that they seemingly should, here are a few things to check:>• Make sure the object has simple collision. The traces used by the rain and snow only check for simple collision.
• Make sure the collision profile of the object is set to block the trace channel selected on UDW as "Rain/Snow Particle Collision Channel". By default this is Visibility. Also make sure the collision response is Collision Enabled or Query Only, as queries are what the rain/snow uses.
• If rain or snow is coming through the roof of a building with a very tall ceiling, it may be that the particles aren't checking high enough for the ceiling when they spawn in. You can adjust this distance using "Ceiling Check Height" on UDW.
-----
VOLUMETRIC CLOUDS NOT SHOWING/BROKEN IN VR
-----
In 4.26 (and also UE5 as of this writing) Unreal's volumetric cloud rendering does not work in VR. It renders correctly only in one eye of the HMD.
In these versions, the problem is an engine limitation so there is no fix. The only solution in these versions is to use a different non-volumetric sky mode. 2D Dynamic Clouds and Static Clouds will work fine in VR.
4.27 has a fix for this which allows volumetric clouds to render in VR correctly. If you need volumetric clouds in VR, I would recommend using 4.27.
-----
VOLUMETRIC FOG IS DARK/CREATES A HARD CUTOFF IN THE FOG
-----
If enabling volumetric fog causes the nearby fog to lose its lighting, and produce a dark line where the local fog meets non-volumetric fog, this is caused by incompatibility with the real time sky light capture.
Volumetric fog cannot recieve light from a real time captured sky light. It's just a limitation of the engine currently.
For this reason, if you're using volumetric fog, I'd recommend changing the Sky Light Mode to "Cubemap with Dynamic Color Tinting" which doesn't rely on real time capturing. It will light the volumetric fog correctly.
-----
LIGHT ARTIFACTS WHEN INSIDE VOLUMETRIC CLOUDS
-----
When going up into the volumetric cloud layer you might notice banding/noise or other light artifacts in the volumetric rendering while in the layer.
The settings are optimized to prioritize quality from the ground, so this is normal for default settings. Here are a few settings to try adjusting to improve render quality within the layer:>• Increase "View Sample Count Scale" This scales the number of samples used in the volumetric rendering. Increasing it will reduce noise in the resolve and can fix some 
artifacts if pushed high enough. Note that this will increase the performance demand of the clouds proportional to the amount you increase the setting.
• Increase "Shadow Sample Scale". This will reduce banding of shadows and make them have a smoother falloff. Again, comes with extra performance cost.
• Increase "Distance to Sample Max Count" in the advanced dropdown. This can help in particular with the horizontal band of light that can be seen from within the cloud layer.
• Reduce "Tracing Max Distance". This can also help reduce the horizontal band of light, without adjusting sample quality. But it also has an effect on the look and performance of clouds as you go below or above the layer.
-----
BLURRY BLACK LIGHTING ARTIFACTS ON MESHES
-----
If you're seeing black noisy artifacts like out of place shadows on meshes, those are probably artifacts coming from Distance Field Ambient Occlusion.
DFAO will be enabled by default if your project settings have "Generate Mesh Distance Fields" enabled.
Artifacts in DFAO are typically caused by the distance field for the object not matching the surface closely enough. In the settings for the static mesh, you might try changing its Distance Field Resolution Scale in the build settings.
You could also just disable the mesh's contribution to DFAO by turning off "Affect Distance Field Lighting" on the mesh.
If you decide you don't want DFAO at all, you can disable that by turning off "Sky Light Casts Shadows" in the Sky Light category.
-----
BLACK NOISE ARTIFACTS WITH YELLOW WARNING TEXT ON MESHES
-----
If you're seeing flickering black pixel noise on certain materials, possibly with a yellow warning message visible in the black space, the problem is probably a bad implementation of pixel depth offset on the material.
The black space + yellow warning text means that the pixel is rendering nothing due to the material being broken for that pixel. This can happen due to pixel depth offset, so the first thing I would recommend is to disconnect the Pixel Depth Offset output from the material, if it has one.
-----
SKY LIGHT / SKY REFLECTIONS UPDATE AT LOW FRAMERATE
-----
If you notice that reflections of the sky or the colors of sky lighting seem to update at a low framerate, the cause is an optimization called Time Slicing which is enabled by default for real time captured sky lights.
This is a very valuable optimization which spreads the render of the sky light capture out over several frames. Unless performance is not a concern, I'd recommend keeping it enabled.
If you'd like to disable it, you can do so from the Captured Sky Light category on UDS. The setting is "Real Time Capture Uses Time Slicing".
-----
EVERYTHING RENDERING BLACK AFTER ADDING UDS
-----
If after adding UDS to your scene, the entire level renders black, the cause is almost certainly exposure settings. Here's a few things to try:>• In your scene, check to see if you have any post process volumes which are controlling the exposure settings. If you do, disable those overrides so UDS can control exposure.
• In Project Settings, check the rendering setting "Extend Default Luminance Range in Auto Exposure Settings". If it's enabled, disable it and restart the editor.
• On UDS, try disabling "Use Exposure Range" in the exposure category.
-----
VOLUMETRIC CLOUDS LOOK BLURRY/STREAKY WHEN MOVING FAST
-----
By default, the volumetric clouds use a rendering mode which uses a long tail of temporal data. Because of this, when the clouds move fast, like during a time lapse, the rendering can become blurry or ghosted.
The solution is to use any of the other rendering modes. You can change the Volumetric Cloud Rendering Mode from the Volumetric Clouds category on UDS.
-----
WEATHER SOUNDS GO QUIET AT INCORRECT TIMES
-----
By default, the weather sounds on UDW use a simple system of sound occlusion to dim and muffle weather when inside interiors.
If you're noticing this happen at incorrect times, it's probably because the occlusion traces are hitting surfaces they shouldn't. You can adjust the behavior of the occlusion system (or disable it completely) from the Sound Occlusion category on UDW.
-----
WATER/OCEAN SHADER LIGHTS INCORRECTLY IN CLOUDY WEATHER
-----
If using some types of water or ocean shaders, you might notice in cloudy weather that the sun or moon appear to affect the material despite being blocked by clouds. This would be because some materials like this test the intensity and color of the active directional light without factoring in light functions.
The solution is to enable a setting on UDS, in the Basic Controls category, called "Dim Directional Lights With Cloud Coverage". This will reduce directional light intensity when cloudy so that most water shaders like this will be able to function correctly.
-----
VOLUMETRIC CLOUDS ARE TOO DARK / GRAY
-----
If the volumetric clouds look unnatrually dark, the problem is probably the directional light affecting them.
Often, this will happen if you've selected "custom actor" for the sun or moon. The built in sun and moon lights have a particular setting customized which you would need to apply to your own light to have them light volumetric clouds well. The setting is "Cloud Scattered Luminance Scale". For best results I would suggest copying the exact color from UDS' dir
ectional light components.
If you haven't selected "custom actor", the problem may instead be that you have a directional light in your scene that you've forgotten to delete before adding UDS.
-----
CANNOT ADJUST CLOUD SPEED OR DIRECTION ON UDS
-----
If you're trying to adjust Cloud Speed or Cloud Direction on UDS and cannot, that would be because you have UDW in your scene as well.
If you have UDW in your scene, cloud movement is controlled by the current wind, which is an aspect of the weather. Which is why they aren't controllable directly on UDS.
To change these with UDW in your scene, adjust the variables "Cloud Speed Multiplier" and "Wind Direction" on UDW.