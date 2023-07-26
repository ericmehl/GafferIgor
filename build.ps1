Foreach( $src in @( "startup" ) )
{
    xcopy $src $env:USERPROFILE\gaffer\$src /eisy
}