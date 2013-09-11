include("interval.jl")

function test_interval()
    
    #probamos suma
    assert(Interval(1,3) + Interval(4,5) == Interval(5, 8) )
    assert(Interval(-1, 1) +  Interval(1,3) == Interval(0, 4) )
    assert(Interval(-10, 10) + Interval(-5, 5) == Interval(-15, 15))
    assert(Interval(-Inf, 10) + Interval(2.38, 3.0) == Interval(-Inf, 13))
    assert(Interval(-Inf, Inf) + Interval(2, 6) == Interval(-Inf, Inf))
    
    #probamos resta
    
    
    
    
    
    #probamos multipicacion
    
    
    #probamos division
    
end

test_interval()
