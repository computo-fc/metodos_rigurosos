inlcude("interval.jl")

function test_interval()
    
    #probamos suma
    assert(Interval(1,3) + Interval(4,5) == Interval(5, 8) )
    assert(Interval(-1, 1) +  Interval(1,3) == Interval(0, 4) )
    assert(Interval(-10, 10) + Interval(-5, 5) == Interval(-15, 15))
    assert(Interval(-Inf, 10) + Interval(3.0, 2.0) == Interval(-Inf, 12))
    assert(Interval(-Inf, Inf) + Interval(2, 6) == Interval(-Inf, Inf))
    
    #probamos resta
    
    
    
    #probamos multipicacion
    
    
    #probamos division
    
end
